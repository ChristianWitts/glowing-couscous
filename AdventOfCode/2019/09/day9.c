#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PAUSE_HALT 0
#define PAUSE_OUTPUT 1
#define PAUSE_REQUEST_INPUT 2

#define INT_TYPE long long int
#define INT_TYPE_FORMAT "%lli"

// Takes a decimal opcode and writes the parameter modes into the array.
// `int *parameter_modes` should have enough room for all modes encoded in the opcode.
void determine_param_modes(int opcode, int *parameter_modes) {
	if(opcode == opcode % 100) return; // no param. modes
	
	char buffer[32];
	sprintf(buffer, "%d", opcode);
	
	int number_of_modes = strlen(buffer) - 2;
	for(int i = 0; i < number_of_modes; i++) {
		if(buffer[i] == '1')
			parameter_modes[number_of_modes - i - 1] = 1;
		else if(buffer[i] == '2')
			parameter_modes[number_of_modes - i - 1] = 2;
		else
			parameter_modes[number_of_modes - i - 1] = 0;
	}
	
	return;
}

typedef struct {
	INT_TYPE *data;
	int position;
	int totalLength;
	
	INT_TYPE inputBuffer[16];
	int inputCursor;
	INT_TYPE outputBuffer[16];
	int outputCursor;
	int inputReady;
	
	INT_TYPE relativeBase;
} intcode_machine;

void intcode_free(intcode_machine *m) {
	free(m->data);
}

void intcode_init_from_file(intcode_machine *m, char* fname) {
	m->data = (INT_TYPE*) malloc(sizeof(INT_TYPE) * 1024 * 10);
	
	// Read file
	FILE *input = fopen(fname, "r");
	m->position = 0;
	while( fscanf(input, INT_TYPE_FORMAT ",", &m->data[m->position++]) > 0);
	fclose(input);
	m->position--;
	
	m->totalLength = m->position;
	m->position = 0;
	
	m->inputCursor = 0;
	m->outputCursor = 0;
	memset(m->inputBuffer, 0, sizeof(m->inputBuffer));
	memset(m->outputBuffer, 0, sizeof(m->outputBuffer));
	
	m->inputReady = 0;
	m->relativeBase = 0;
}

// Executes instructions until reaching opcode 03, 04, or 99.
// Returns a PAUSE_* code with the reason execution stopped.
int intcode_run(intcode_machine *m) {
	while(m->position < m->totalLength) {
		int opcode = m->data[m->position] % 100;
		
		int parameter_modes[] = {0, 0, 0};
		determine_param_modes(m->data[m->position], parameter_modes);
		
		INT_TYPE *positions = &m->data[m->position+1];
		INT_TYPE a, b, c;
		
		// Please note the correct usage of switch/case.
		// It's not just "condensed if/elseif/else", you philistines.
		switch(opcode) {
			case 7:
			case 8:
			case 1:
			case 2:
				c = (parameter_modes[2] == 2) ? (positions[2] + m->relativeBase) : positions[2];
			case 5:
			case 6:
				b = (parameter_modes[1] == 0) ? 
					m->data[positions[1]] : (
						(parameter_modes[1] == 2) ?
							m->data[positions[1]+m->relativeBase] : 
							positions[1]
					);
			case 9:
				a = (parameter_modes[0] == 0) ? 
					m->data[positions[0]] : (
						(parameter_modes[0] == 2) ?
							m->data[positions[0]+m->relativeBase] : 
							positions[0]
					);
				break;
		}
		
		if(opcode == 1) {
			m->data[c] = a + b;
			m->position += 4;
		
		} else if(opcode == 2) {
			m->data[c] = a * b;
			m->position += 4;

		// Take input
		} else if(opcode == 3) {
			if(!m->inputReady)
				return PAUSE_REQUEST_INPUT;
			
			m->inputReady = 0;
			
			if(parameter_modes[0] == 2)
				m->data[m->data[m->position+1]+m->relativeBase] = m->inputBuffer[m->inputCursor];
			else
				m->data[m->data[m->position+1]] = m->inputBuffer[m->inputCursor];

			m->position += 2;
			
		// Print output
		} else if(opcode == 4) {
			m->outputCursor = 0;
			if(parameter_modes[0] == 2)
				m->outputBuffer[m->outputCursor] = m->data[m->data[m->position+1]+m->relativeBase];
			else if(parameter_modes[0] == 1)
				m->outputBuffer[m->outputCursor] = m->data[m->position+1];
			else
				m->outputBuffer[m->outputCursor] = m->data[m->data[m->position+1]];
			m->position += 2;
			return PAUSE_OUTPUT;
		
		// Jump if true
		} else if(opcode == 5) {
			if(a) m->position = b; else m->position += 3;
		
		// Jump if false
		} else if(opcode == 6) {
			if(a == 0) m->position = b; else m->position += 3;
		
		// less than
		} else if(opcode == 7) {
			m->data[c] = a < b;
			m->position += 4;
		
		// equals
		} else if(opcode == 8) {
			m->data[c] = a == b;
			m->position += 4;
		
		// Adjust relative base
		} else if(opcode == 9) {
			m->relativeBase += a;
			m->position += 2;
			
		// Halting
		} else if(opcode == 99) {
			return PAUSE_HALT;
		}
	}
	
	printf("WARN: intcode_run exited without opcode 99\n");
	return PAUSE_HALT;
}
int main(int argc, char **argv) {
	if( argc != 2 ) {
		printf("Usage: %s [input file]\n", argv[0]);
		return 1;
	}
		
	// Setup the machine
	intcode_machine m;
	intcode_init_from_file(&m, argv[1]);
	
	// A basic frontend interface for the machine
	int pauseSignal;
	
	do {
		pauseSignal = intcode_run(&m);
		
		if(pauseSignal == PAUSE_OUTPUT) {
			printf(
				"OUTPUT: data[%i] = " INT_TYPE_FORMAT "\n",
				0,
				m.outputBuffer[0]
			);
			
		} else if(pauseSignal == PAUSE_REQUEST_INPUT) {
			printf("Input: ");
			scanf(INT_TYPE_FORMAT, &m.inputBuffer[m.inputCursor]);
			m.inputReady = 1;
		}
		
	} while(pauseSignal != PAUSE_HALT);
	
	intcode_free(&m);
	
	return 0;
}

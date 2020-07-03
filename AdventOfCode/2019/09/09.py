import sys
import itertools

VERBOSE = True

def openFile():
    return open(sys.argv[1], "r")

class IntcodeMachine:
    def __init__(self, data):
        self.memory = data
        self.pointer = 0
        self.size = len(data)
        self.out = 0
        self.halt = False
        self.initialized = False
        self.relBase = 0

    def process(self, inputArg = None):
        if inputArg != None:  
            self.initialized = True
        
        while self.pointer < self.size:
            opcode = int(str(self.memory[self.pointer])[-2:])
            paramModes = str(self.memory[self.pointer])[:-2]
            if (opcode == 99): # HALT
                self.halt = True
                if VERBOSE:
                    print('HALT')
                break
            elif (opcode == 1): # OPCODE 01 - Sum
                self.__setParam(paramModes, 3, self.__getParam(paramModes,1) + self.__getParam(paramModes,2))
                self.pointer += 4
            elif (opcode == 2): # OPCODE 02 - Multiply
                self.__setParam(paramModes, 3, self.__getParam(paramModes,1) * self.__getParam(paramModes,2))
                self.pointer += 4
            elif (opcode == 3):  # OPCODE 03 - Input
                if inputArg != None:
                    self.__setParam(paramModes, 1, inputArg)
                    inputArg = None
                else:
                    if VERBOSE:
                        self.__setParam(paramModes, 1, int(input("Type int > ")))
                    else:
                        break
                self.pointer += 2
            elif (opcode == 4):  # OPCODE 04 - Print
                out = self.__getParam(paramModes,1)
                if VERBOSE:
                    print(">> " + str(out))
                self.out = out
                self.pointer += 2
            # Start of part 2
            elif (opcode == 5):  # OPCODE 05 - JNZ (jump if not zero)
                if (self.__getParam(paramModes,1) != 0):
                    self.pointer = self.__getParam(paramModes,2)
                else:
                    self.pointer += 3
            elif (opcode == 6):  # OPCODE 06 - JZ (jump if zero)
                if (self.__getParam(paramModes,1) == 0):
                    self.pointer = self.__getParam(paramModes,2)
                else:
                    self.pointer += 3
            elif (opcode == 7):  # OPCODE 07 - Set 1 if first is less than second else 0
                if (self.__getParam(paramModes,1) < self.__getParam(paramModes,2)):
                    self.__setParam(paramModes, 3, 1)
                else:
                    self.__setParam(paramModes, 3, 0)
                self.pointer += 4
            elif (opcode == 8):  # OPCODE 08 - Set 1 if first is equal to second else 0
                if (self.__getParam(paramModes,1) == self.__getParam(paramModes,2)):
                    self.__setParam(paramModes, 3, 1)
                else:
                    self.__setParam(paramModes, 3, 0)
                self.pointer += 4
            elif opcode == 9:
                self.relBase += self.__getParam(paramModes,1)
                self.pointer += 2
            else:
                print(str(self.memory[self.pointer]) + " Something went wrong :(")
                break

    def __getParam(self, paramModes, param):
        return self.memory[self.__getParamAddress(paramModes, param)]

    def __setParam(self, paramModes, param, value):
        self.memory[self.__getParamAddress(paramModes, param)] = value
    
    def __getParamAddress(self, paramModes, param):
        type = 0
        try:
            type = int(paramModes[-param])
        except:
            pass
        if type == 0:
            return self.memory[self.pointer + param]
        elif type == 1:
            return self.pointer + param
        elif type == 2:
            offset = self.memory[self.pointer + param]
            return self.relBase + offset
        else:
            print('Param type error')
            return 0

def challenges():
    """
    Improved and tested intcode machine
    """
    file = openFile()
    data = list(map(lambda x: int(x), file.read().split(','))) + [0 for i in range(10000)]
    machine = IntcodeMachine(data)
    machine.process()
    file.close()

challenges()


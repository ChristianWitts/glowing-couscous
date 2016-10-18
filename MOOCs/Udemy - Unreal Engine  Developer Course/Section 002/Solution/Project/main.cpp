#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

void PrintIntro();
string GetGuess();

int main() 
{
	PrintIntro();
	string Guess = GetGuess();
	
	// repeat the guess back to the player
	cout << "Your guess was: " << Guess << endl;

	cout << endl;
	return 0;
}

void PrintIntro() {
	// Introduce the game
	constexpr int WORD_LENGTH = 5;
	cout << "Welcome to Bulls & Cows, a fun word game." << endl;
	cout << "Can you guess the " << WORD_LENGTH
		<< " letter isogram I'm thinking of ?" << endl;

	return;
}

string GetGuess() {
	// get a guess from the player
	cout << endl << "Enter your guess: ";
	string Guess = "";
	getline(cin, Guess);

	return Guess;
}
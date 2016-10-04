#ifndef CHAPTER1_HPP
#define CHAPTER1_HPP

#include <SFML/Graphics.hpp>

class Game
{
	public:
								Game();
		void					run();

	private:
		void					processEvents();
		void					update(sf::Time deltaTime);
		void					render();
		void					handlePlayerInput(sf::Keyboard::Key key, bool isPressed);

	private:
		sf::RenderWindow		mWindow;
		sf::CircleShape			mPlayer;
		bool					mIsMovingUp;
		bool					mIsMovingDown;
		bool					mIsMovingRight;
		bool					mIsMovingLeft;

		static const sf::Time	TimePerFrame;
};

#endif
#ifndef CHAPTER2_HPP
#define CHAPTER2_HPP

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
		sf::Texture				mTexture;
		sf::Sprite				mPlayer;
		bool					mIsMovingUp;
		bool					mIsMovingDown;
		bool					mIsMovingRight;
		bool					mIsMovingLeft;

		static const sf::Time	TimePerFrame;
};

#endif
#ifndef CHAPTER2_HPP
#define CHAPTER2_HPP

#include <SFML/Graphics.hpp>

class TextureHolder
{
	private:
		std::map<Textures::ID,
			std::_unique_ptr<sf::Texture>> mTextureMap;

};

#endif
//
// Created by Chris on 2016/10/03.
//
#include <iostream>

int main()
{
    int sum = 0, value = 0;
    // Read until EOF, calculating a running total of all values read
    while (std::cin >> value)
        sum += value;

    std::cout << "Sum is: " << sum << std::endl;
    return 0;
}

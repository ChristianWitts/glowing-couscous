//
// Created by Chris on 2016/10/03.
//
#include <iostream>

int main()
{
    int sum = 0;
    // Sum values from 1 through 10 inclusive
    for (int val = 1; val <= 10; ++val)
        sum += val;     // Equivalent to sum = sum + val

    std::cout << "Sum of 1 to 10 inclusive is "
              << sum << std::endl;

    return 0;
}

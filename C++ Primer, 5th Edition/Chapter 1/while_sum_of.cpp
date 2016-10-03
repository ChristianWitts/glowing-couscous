//
// Created by Chris on 2016/10/03.
//

#include <iostream>

int main()
{
    int sum = 0, val = 1;
    // Keep executing as long as val is <= 10
    while (val <= 0) {
        sum += val;     // increment sum by val
        ++val;          // increment val by 1
    }
    std::cout << "Sum of 1 to 10 inclusive is "
              << sum << std::endl;

    return 0;
}
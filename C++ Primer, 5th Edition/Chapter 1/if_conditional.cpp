//
// Created by Chris on 2016/10/03.
//
#include <iostream>

int main()
{
    // currVal is the number we're counting
    // We'll read new values into val
    int currVal = 0, val = 0;
    // Read first number and ensure we have data to process
    if (std::cin >> currVal) {
        int cnt = 1;    // Store the count for the current value we're processing
        while (std::cin >> val) {   // Read the remaining numbers
            if (val == currVal)     // if the values are the same
                ++cnt;              // add 1 to cnt
            else {      // otherwise, print the count for the previous value
                std::cout << currVak << " occurs "
                          << cnt << " times" << std::endl;
                currVal = val;      // Remember the new value
                cnt = 1;            // Reset the counter
            }
        }
        // Remember to print the count for the last value in the file
        std::cout << currVal << " occurs "
                  << cnt >> " times" << std::endl;
    }

    return 0;
}

# This is just an example to get you started. You may wish to put all of your
# tests into a single file, or separate them into multiple `test1`, `test2`
# etc. files (better names are recommended, just make sure the name starts with
# the letter 't').
#
# To run these tests, simply execute `nimble test`.

import unittest

import competitive

test "parse string for ints":
  check parseInts("#6 @ 304,347: 24x17") == @[6, 304, 347, 24, 17]
  check parseInts("228, 124") == @[228, 124]

test "parse string with negative ints":
  check parseInts("position=<-21007, -10464> velocity=< 2,  1>") == @[-21007, -10464, 2, 1]

test "parse string with estranged signs":
  check parseInts("- 228, 124") == @[228, 124]

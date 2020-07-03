# Package

version       = "0.1.0"
author        = "Christian Witts"
description   = "A library with some competitive programming helpers"
license       = "MIT"
srcDir        = "src"


# Dependencies

requires "nim >= 0.19.0"

task clean, "Clean up build/test artifacts":
    exec "fd -t x -x rm {}"

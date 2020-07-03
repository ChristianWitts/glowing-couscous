import sets, strutils

{.deadCodeElim: on.}

{.push debugger:off .}
include "system/inclrtl"
{.pop.}

const
  AsciiDigitCodes = toSet([43, 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])
    ## Number 0..9 and +-

proc digitsOnly(): seq[(string, string)] {.noSideEffect, raises: [], tags: [].} =
  ## Generate a mapping sequence of non-digit ASCII characters to whitespace.
  for c in 0..255:
    if not AsciiDigitCodes.contains(c):
      result.add(($char(c), " "))

const
  DigitsOnly* = digitsOnly()
    ## DigitsOnly is a sequence of mappings for all non-digits to whitespace.
    ## It is for use in string.multiReplace, akin to Python's translation tables
    ## found in ``string.maketrans`` & ``string.translate``.

proc parseInts*(s: string): seq[int] {.noSideEffect, raises: [OverflowError], tags: [].} =
  for token in tokenize(s.multiReplace(DigitsOnly)):
    if not token.isSep:
      try:
        result.add(token.token.parseInt)
      except ValueError:
        continue

# Parse into a tuple container
# take varnames via varargs or string
# template the type generation
# return boxed tuple

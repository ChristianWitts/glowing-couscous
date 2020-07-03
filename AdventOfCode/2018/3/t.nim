import strutils, pegs, strformat

var
  translationTable: seq[(string, string)]
  # charStr = newStringOfCap(1)

for c in 0..255:
  # add(charStr, c)
  if c <= 47 or c >= 58:
    translationTable.add(($char(c), " "))
  # charStr = ""

# #1253 @ 683,604: 22x23

# echo translationTable

var
  s: string = "#1253 @ 683,604: 22x23"

echo s.multiReplace(translationTable)

for token in tokenize(s.multiReplace(translationTable)):
  echo token
  if not token.isSep:
    echo token.token.parseInt()

# if s =~ peg"\d+":
#   echo matches[0]

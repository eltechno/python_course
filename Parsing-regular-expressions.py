
import re
ingredient = "Harina: 2 Cups"
pattern_text = r'(?P<ingredient>\w+):\s+(?P<amount>\d+)\s+(?P<unit>\w+)'
# r' prefijo que ayuda a python a no leer \
"""
\w+ replace words
\W chacacter that's not a letter of digit
\d+ replace digits
\D character that's not a digit
\s+ spaces
\S character that's not some kind of space or tab (invisible)
?P<name> data que queremos rastrear
el : pertenece a el string original
+ as a suffix means to match one or more of the preceding patterns
* as a suffix which matches zero of more of the preceding patterns
\w* matches zero o more characters
to match a * need to use \*
? as suffix, matches zero of one of the preceding expressions
. matches any single character
"""

pattern = re.compile(r'(?P<ingredient>\w+):\s+(?P<amount>\d+)\s+(?P<unit>\w+)')
match = pattern.match(ingredient)
#print(match)
print(match.group())
print(match.group('ingredient'))
print(match.group('amount'))
print(match.group('unit'))

ingredient_pattern = re.compile(
r'(?P<ingredient>\w+):\s+' #name of the ingredient up to the ":"
r'(?P<amount>\d+)\s+' #amount. all the digits up to space
r'(?P<unit>\w+)'      #units aphanumeric characters
)

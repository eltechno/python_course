"""
The second part of the website project is to write a script that validates the password entered by the user.
The company also puts some rules in order to verify valid passwords:

It can contain lowercase a-z and uppercase letters A-Z
It can contain numbers
It can contain the symbols: *, #, $, %, !, &, .
It must be at least 8 characters long but not more than 20
Your colleague also gave you a list of passwords as examples to test.
"""


import re
passwords = ['Apple34!rose', 'My87hou#4$', 'abc123']

# Write a regex to match a valid password
regex = r"[a-zA-Z0-9*#\$%!&\.]{8,20}"

for example in passwords:
  	# Scan the strings to find a match
    if re.search(regex, example):
        # Complete the format method to print out the result
      	print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
      	print("The password {pass_example} is invalid".format(pass_example=example))
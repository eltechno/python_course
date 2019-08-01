"""
A colleague has asked for your help! When a user signs up on the company website, they must provide a
valid email address.
The company puts some rules in place to verify that the given email address is valid:

The first part can contain:
Upper A-Z and lowercase letters a-z
Numbers
Characters: !, #, %, &, *, $, .
Must have @
Domain:
Can contain any word characters
But only .com ending is allowed
The project consist of writing a script that checks if the email address follow the correct
pattern. Your colleague gave you a list of email addresses as examples to test.
"""

import re
emails= ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']

# Write a regex to match a valid email address
regex = r"[a-zA-Z0-9!#%&*\$\.]+@\w+\.com"

for example in emails:
  	# Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
      	print("The email {email_example} is a valid email".format(email_example=example))
    else:
      	print("The email {email_example} is invalid".format(email_example=example))
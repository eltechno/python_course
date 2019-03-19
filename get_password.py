#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 18/03/19

#Feature:  #Enter feature name here
# this is how to get password works
# only works in linux CLI not in here

#Scenario:  # Enter scenario name here
# Enter steps here
import getpass
password_text = getpass.getpass()
confirming_password_text = getpass.getpass("Confirm:")

while password_text != confirming_password_text:
    password_text = getpass.getpass()
    confirming_password_text = getpass.getpass("Confirm:")
    assert password_text == confirming_password_text

p = getpass.getpass("Enter Password")
print ('You entered', p )



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 15/03/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here
#! /usr/bin/python

import os
import socket
import hashlib
import struct
"""""
This is a simple script to play with md5
"""""
# get the host id and host name to calculate the hostkey
hostid=os.popen("hostid").read().strip()
""" this is a test """

hostname = socket.gethostname()
ioukey=int(hostid,16)
for x in hostname:
 ioukey = ioukey + ord(x)
print("ioukey ===", ioukey)
print("hostid=" + hostid +", hostname="+ hostname + ", ioukey=" + hex(ioukey)[2:])

# create the license using md5sum
iouPad1 = b'\x4B\x58\x21\x81\x56\x7B\x0D\xF3\x21\x43\x9B\x7E\xAC\x1D\xE6\x8A'
iouPad2 = b'\x80' + 39 * b'\0'
md5input=iouPad1 + iouPad2 + struct.pack('!I', ioukey) + iouPad1
print ("md5input ===", md5input)
iouIncense=hashlib.md5(md5input).hexdigest()[:16]
print ("incense ===", iouIncense)

# add license info to $HOME/.ioucr
print ("*" * 70)
print ("Create the license file $HOME/.ioucr with this command:")
print (" echo -e '[license]" + hostname + " = " + iouIncense + ";'" + " | tee $HOME/.ioucr ")
print ('\n'+"The command adds the following text to $HOME/.ioucr:")
print ("[license]"+'\n' + hostname + " = " + iouIncense + ";")
# disable Lan line home feature
print ("*" * 70)
print ("Disable the line line home feature with this command:")
print (" grep -q -F '127.0.0.1 xml.crisco.com' /etc/hosts || echo '127.0.0.1 xml.crisco.com' | sudo tee -a /etc/hosts")
print ("\n"+ "The command adds the following text to /etc/hosts:")
print ("127.0.0.1 xml.crisco.com")
print ("*" * 70)
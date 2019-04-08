#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 5/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import socket
import psutil

hostname = socket.gethostname()
print(hostname)

memoria = psutil.virtual_memory()


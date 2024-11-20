#!/usr/bin/python
from __future__ import unicode_literals

import subprocess
import json
import sys
import re
import os

def list1 (p) :
	f = {}
	y = 10
	result = y + p
	f[p] = result
	print(result)
	print(f)
	return result

def program () :
	x = int(input())
	if x == 0:
		print("Program aborted")
		return
	if x >= 1 and x <= 999:
		list1 (x)
		program()
	else :
		print ("Invalid number entered. Try Again")
		program()


print ("Please enter a number between 1 ands 999. \nEnter 0 to abort program.")
program()


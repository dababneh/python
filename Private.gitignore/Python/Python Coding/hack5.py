#!/usr/bin/python
from __future__ import unicode_literals

import subprocess
import json
import sys
import re
import os

print ("Enter your name")
x = raw_input()
print ("\nEnter your age")
y = input()

class Person:
  def __init__(now, name, age):
    now.name = name
    now.age = age

p1 = Person(x, y)

print("\nThe Following name has been registered")
print(p1.name, p1.age)

from selenium import webdrivers 
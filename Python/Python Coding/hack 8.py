#!/usr/local/bin/python3

import os
import sys
import string

class function :
    def __init__(self, word, rot) : 
        self.word = word
        self.rot = rot 

    def rotate_right (self) :

        k = rot
        print("\nShifting to the right : \n")
        print (word[-k:] + word[:-k])
        return print("\nThank you for using the program\n")

    def rotate_left(self) :

        k = rot
        print("\nShifting to the left : \n")
        print (word[k:] + word[:k])
        return print("\nThank you for using the program\n")
    

try : 
    print("\nHello there, this program will allow you to rotate any word or phrase. Lets get started.\n")      
    word = input("Enter a word : ")
    print(len(word))
    rot = int(input("\nEnter number of rotation : "))
    direction = input("\nWhich direction do you want, Right or Left? : ")
    direction = direction.upper()
    func = function(word,rot)
    print("\n" +func.word, ":" ,func.rot,  "\n")
    if direction == "RIGHT":
        func.rotate_right()
    elif direction == "LEFT":
        func.rotate_left()
    else :
        print("Invalid input. You seriously only had one job. You do not deserve our program.")
except :
    print("unkown error. Seriously what have you done?")


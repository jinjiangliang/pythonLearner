# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 15:07:57 2018

@author: 1000877

Video 1.3.8: Writing Simple Functions

import random
random.choice([1,2,3,4])
random.choice("abcdef")
"""
'''
need
import random

'''
def password(length):
    pw = str()
    characters = "abcdefghijklmn" + "0123456789"
    for i in range(length):
        pw = pw + random.choice(characters)
    return pw    
'''
"a"+"b"

def is_vowel(letter):
   if letter in ["a","e","i","o","u"]:
     return(True)
   else:
     return(False)

def is_vowel(letter):
   if letter in "aeiou":
     return(True)
   else:
     return(False)
     
letter in 'aeiouy' is a condition that will test this. For completeness, you might also check that the input is a string, and contains only one character.     
4 is not a string , and Python cannot test if an int is in a string .
'''    
def is_vowel(letter): 
    if type(letter) == int: 
        letter = str(letter) 
    if letter in "aeiouy": 
        return(True) 
    else: 
        return(False)
        
def factorial(n):
   if n == 0:
     return 1
   else:
     N = 1
     for i in range(1, n+1):
       #blank#
       N *= i
     return(N)
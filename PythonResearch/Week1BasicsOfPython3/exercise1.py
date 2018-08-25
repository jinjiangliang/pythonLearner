# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 15:38:27 2018

@author: 1000877

Import the string library.
Create a variable alphabet that consists of the lowercase 
and uppercase letters in the English alphabet 
using the ascii_letters data attribute of 
the string library.
"""

import string

alphabet = string.ascii_letters

'''
1b)
The lower and upper cases of the English alphabet 
are stored as the string alphabet.
Consider the sentence 
'Jim quickly realized that the beautiful gowns 
are expensive'. 
Create a dictionary count_letters 
with keys consisting of each unique letter 
in the sentence and 
values consisting of the number of times 
each letter is used in this sentence. 
Count upper case and lower case letters 
separately in the dictionary.
'''

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}

for letter in sentence:
    if letter in alphabet:
        if letter in count_letters.keys():
            count_letters[letter] +=1
        else:
            count_letters[letter] =1
'''
Exercise 1c
Rewrite your code from 1b to make a function called counter that takes a string input_string and returns a dictionary of letter counts count_letters. If you were unable to complete 1b, you can use the solution by selecting Show Answer.
Use your function to call counter(sentence).
'''
def counter(sentence):
    count_letters = {}
# counting
    for letter in sentence:
        if letter in alphabet:
            if letter in count_letters.keys():
                count_letters[letter] +=1
            else:
                count_letters[letter] =1
    return count_letters
# test the function
counter(sentence)

'''
Abraham Lincoln was a president 
during the American Civil War. 
His famous 1863 Gettysburg Address has been stored as address, 
and the counter function as defined in part 1c has been loaded. 
Use these to return a dictionary consisting of the count of 
each letter in this address, and save this as address_count.

Print address_count.
'''
F = open("Lincoln1863.txt", "w")

F.write("'                                                                                                 Four score and seven years ago our fathers brought forth  \\\nNow we are engaged in a great civil war  testing whether that nation  or any nation so conceived                                   and so dedicated         \n\n                                                                                                                                upon this continent  \\\nNow we are engaged in a great civil war  testing whether that nation  or any nation so conceived   can long endure. We are met on a great battle...   \n\n                                                                                                                                       a new nation  \\\nNow we are engaged in a great civil war  testing whether that nation  or any nation so conceived   as a final resting place for those who died here   \n\n                                                                                                                      conceived in liberty  \\\nNow we are engaged in a great civil war  testing whether that nation  or any nation so conceived   that the nation might live. This we may   \n\n                                                                                                  and dedicated to the proposition that all men are created equal.  \nNow we are engaged in a great civil war  testing whether that nation  or any nation so conceived                               in all propriety do.   ")

F.close

F = open("input.txt", "w") 
F.write("Hello\nWorld") 
F.close() 

address = ("'                                                                                                 Four score and seven years ago our fathers brought forth  \\\nNow we are engaged in a great civil war  testing whether that nation  or any nation so conceived                                   and so dedicated         \n\n                                                                                                                                upon this continent  \\\nNow we are engaged in a great civil war  testing whether that nation  or any nation so conceived   can long endure. We are met on a great battle...   \n\n                                                                                                                                       a new nation  \\\nNow we are engaged in a great civil war  testing whether that nation  or any nation so conceived   as a final resting place for those who died here   \n\n                                                                                                                      conceived in liberty  \\\nNow we are engaged in a great civil war  testing whether that nation  or any nation so conceived   that the nation might live. This we may   \n\n                                                                                                  and dedicated to the proposition that all men are created equal.  \nNow we are engaged in a great civil war  testing whether that nation  or any nation so conceived                               in all propriety do.   ")
address_count = counter(address)
print(address_count)
'''
1e
The frequency of each letter in the Gettysburg Address is already stored as address_count. Use this dictionary to find the most common letter in the Gettysburg address.
Store this letter as most_frequent_letter, and print your answer.
'''
v = list(address_count.values())
k = list(address_count.keys())
most_frequent_letter = k[v.index(max(v))]
print(most_frequent_letter)
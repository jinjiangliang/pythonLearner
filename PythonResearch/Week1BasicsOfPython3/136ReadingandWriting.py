# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 20:41:40 2018

@author: 1000877

Video 1.3.6: Reading and Writing Files


"""
filename = "input.txt"

for line in open (filename):
    print(line)

'''
\n
'''
for line in open (filename):
    line = line.rstrip()
    print(line)
    
for line in open (filename):
    line = line.rstrip().split(" ")
    print(line)
    
F = open("output.txt", "w")

F.write("Python\n")

F.close

F = open("input.txt", "w") 
F.write("Hello\nWorld") 
F.close() 
lines = [] 
for line in open("input.txt"): 
    lines.append(line.strip()) 
print(lines) 
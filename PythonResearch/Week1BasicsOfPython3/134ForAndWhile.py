# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 19:59:49 2018

@author: 1000877

Video 1.3.4: For and While Loops

"""

for x in range(10):
    print(x)
    
names = ["Tom","Tim"]    
    
for name in names:
    print(name)
    
for i in range(len(names)):
    print(names[i])
    
age = {'Jim':39}

age.keys()

for name in age.keys():
    print(name,age[name])
    
for name in age:
    print(name,age[name])
    
for name in sorted(age.keys()):
    print(name,age[name])

for name in sorted(age.keys(), reverse = True):
    print(name,age[name])
    
'''
For loop: set number of iterations
'''
bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}

for bear in bears:
  if (bears[bear] == "friendly"):
   print("Hello, "+bear+" bear!")
else:
  print("odd")
  


is_prime = True
n=97
for i in range(2,n):
   if n%i == 0:
     is_prime = False
     #blank#
print(is_prime)

n=100
number_of_times = 0
while n >= 1:
   n //= 2
   number_of_times += 1
print(number_of_times)

'''
This code will repeatedly divide a a number, beginning with 100, by 2 (rounding down to remain an integer). This process will stop once this process produces 1 or less. 7 is the number of steps required for this to occur.
'''

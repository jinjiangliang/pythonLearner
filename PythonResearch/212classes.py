# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 19:24:18 2018

@author: 1000877

Video 2.1.2: Classes and Object-Oriented Programming
object: internal data, methods;
class: create own object;
inheritance
"""

ml = [3,4,6,8,7,9]
ml.sort()

class Mylist(list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))
    '''
    specify inheritance with ()
    '''
'''
an instance of that type
'''

x= [3,5,4]
min(x)
max(x)
x.remove(10)

y = Mylist(x)


'''
class NewList(list): 
   def remove_max(self): 
     self.remove(max(self)) 
   def append_sum(self): 
     self.append(sum(self)) 

x = NewList([1,2,3]) 
while max(x) < 10: 
   x.remove_max() 
   x.append_sum() 
print(x) 

What will this print?
Nothing: this program will never halt. 
...
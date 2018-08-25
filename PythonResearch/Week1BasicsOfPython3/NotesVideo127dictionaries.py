# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:08:05 2018

@author: 1000877

1.2.7: Dictionaries
Review Python dictionaries and the key-value pairs they contain
Understand the dynamically updated view objects dict.keys(), dict.values(), and dict.items()
key: value pairs;
key: immutable;
//


"""
age = {}
age = dict()
age = {"Tim":29, "Jim":31,"pam":27}
age["Tim"]
age["Tim'] += 1
   
   '''
type, view object
'''
names = age.keys()
type(names)
age["Tom"] = 50
names
'''
the content of view object change automaticly.
'''
ages = age.values
age["Nick"] = 31
names
ages
'''
membership
'''
"Tom" in age
"Zofia" in age

'''
Dictionary keys are not mutable.
Only immutable types are allowed as keys.
string and tuples can be used,
lists cannot.
'''

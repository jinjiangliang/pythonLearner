# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 17:43:35 2018

@author: 1000877

Video 1.3.2: Copies

Shallow copy
a copy of x
and references to a,b

Deep copy
a copy of x
and a copy of a, b as well;

copy.copy creates a shallow copy, 
which constructs a new object 
whose contents refer to the original object to the greatest extent possible. In contrast, copy.deepcopy creates a deep copy, creating both a new variable name as well as a new object with new content, but equal values to the original. 
Therefore, y and z refer to different objects.
"""


# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 15:13:27 2018

@author: 1000877
Video 1.1.5: Random Choice

"""

import random
random.choice([2,44,55,66])
random.choice([2,"aa",55,66])
print(random.choice([2,"aa",55,66]))

"""
True or false: random.choice will not work on immutable types.
False: random.choice only requires that the object has several values regardless of mutability. correct
"""
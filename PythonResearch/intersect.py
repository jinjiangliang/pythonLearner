# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 15:04:10 2018

@author: 1000877
Video 1.3.8: Writing Simple Functions

"""

def intersect(s1,s2):
    res = []
    for x in s1:
        if x in s2:
            res.append(x)
    return res

'''
intersect([1,2],[2,3])
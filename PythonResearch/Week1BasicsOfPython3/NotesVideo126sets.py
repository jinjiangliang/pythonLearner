# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:59:37 2018

@author: 1000877

1.2.6: Sets
Review Python sets and the differences between a set and a frozenset
Review basic set operations
hashable
not ordered
//
Set, mutable
frozen set, not mutable
cannot be indexed.
elements can never be duplicated
distinct elements
"""
ids = set()
ids = set([1,2,4,6,7,8,9])
len(ids)
ids.add(10)
ids.add(2)
'''
nothing happens
'''
ids.pop()
ids
ids = set(range(10))
males = set([1,3,5,6,7])
females = ids-males
everyone = males | females
everyone & set([1,2,3])
word = "antidisestablishmentarianism"
letters = set(word)
len(letters)
x = {1,2,3}
y = {2,3,4}
y-x
x & y
x.intersection(y)
 
(x-y) | (y-x)
x.symmetric_difference(y)

x.issubset(y)
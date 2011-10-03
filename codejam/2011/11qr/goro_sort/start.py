#!/usr/bin/python3
import math
import sys
import itertools
from functools import reduce
import random

def printe(*st):
   sys.stderr.write(",".join([str(x) for x in st])+"\n")
        
def simulate():
   input()
   n = [int(i) for i in input().split()]   
   print(n)         

def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))
    


def find(s):
#   print("x",s)
   l = list(random_permutation(s))
   s = sorted(l)
   x = 0
#   print(l,s)
   while x < len(l):
      if l[x] == s[x]:
         s.pop(x)
         l.pop(x)
      else:
         x += 1
   return s

def w(s):
   i = 0
   while len(s)>0:
      s = find(s)
      i += 1
   return i

t = 100
d = [l for l in range(1,22)]
a = 0
for i in range(t):   
   a += w(d)
print(a/t)

t = 4
l = {}

for x in range(t+1):
   l[x] = 0
   
   
for p in itertools.permutations([i for i in range(1,t+1)]):
   s = 0
   for i in range(t):
      if (i + 1) == p[i]:
         s += 1
   l[s] += 1
   if s==1:
      print(p,s)
print(l)

if __name__ == 'x__main__':
   for i in range(int(input())):
      print("Case #{}: {}".format(i+1,simulate()))

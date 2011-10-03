#!/usr/bin/python3
import math
import sys
import itertools
from functools import reduce
import random
from decimal import Decimal

tv = {}
mv = {}
fv = {}
bcv = {}



def factorial(n):
   if n in fv:
      return fv[n]    
   if n==1:
      return 1
   elif n == 0:
      return 0
   else:
      fv[n] = factorial(n-1) * n
      return fv[n]

def bc2(n,k):
   return int(factorial(n) / factorial(k) / factorial(n-k))

def bc(n, k):
    if (n,k) in bcv:
       return bcv[(n,k)]  
    if (k==1):
       return n
    v = int(bc(n,k-1) * (n-k+1) / k)
    bcv[(n,k)] = v
    return v

def printe(*st):
   sys.stderr.write(",".join([str(x) for x in st])+"\n")



   

def t(n,k):
   if (n,k) in tv:
      return tv[(n,k)]
   if (n==k):
      return 1
   elif n == k + 1:
      return 0
   elif k == 0:
      l = factorial(n)
      for i in range(1,n+1):
         l -= t(n,i)
      tv[(n,k)] = l
      return l
   else:
      tv[(n,k)] = bc(n,k) * t(n - k, 0)
      return tv[(n,k)]

def m(n):
   if n in mv:
      return mv[n]
   if n == 1:
      return 0
   if n == 2:
      return 2
   if n==0:
      return 0
   
   v = Decimal(t(n,0))
   for i in range(1,n):
      v += t(n,i) * (m(n-i) + 1)
   v += 1
   if factorial(n) == t(n,0):
      return 0
   v = v / (factorial(n) - t(n,0))
   mv[n] = v
   return v            
   
for i in range(1000):
   t(i,0)   
   m(i)
   printe(i)
   
def simulate():
   input()
   n = [int(i) for i in input().split()]
   s = 0   
   for i in range(len(n)):
      if n[i] != i + 1:
         s +=1
   return m(s)
      


if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{}: {:.6f}".format(i+1,simulate()))
      
      

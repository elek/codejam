#!/usr/bin/python
from math import factorial
import math

memoize = {}

def nk(n,k):
   return round(factorial(n) / (factorial(k) * factorial(n-k)))
MOD = 100003

def process(maxn,size):
   if (maxn,size) in memoize:
      return memoize[(maxn,size)]
      
   if size == 1:
      return 1
   if size == maxn - 1:
      return 1
   else:
      bor = maxn - size - 1
      
      f = max(size - 2 - bor , 0)
      to = size - 2 
      c = 0
      for i in range(f, to + 1):
         b = size - 2 - i
         c += (process(size,i + 1) * nk(bor,b)) % MOD
      res = c % MOD
      memoize[(maxn,size)] = res
      return res
   
         
         
def calc(n):
   c = 0
   for i in range(1,n):
      c += process(n,i)
   return c % MOD


if __name__ == '__main__':   
   for i in range(int(input())):
      print("Case #{0}: {1}".format(i+1,calc(int(input()))))
         
         


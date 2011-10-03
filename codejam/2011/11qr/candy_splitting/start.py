#!/usr/bin/python3
import math
import sys
import itertools
from functools import reduce

def printe(*st):
#   sys.stderr.write(",".join([str(x) for x in st])+"\n")
   return
   

      
def brute_force(n):
   mx = -1
   for i in range(1,2**len(n)-1):
      g1 = []
      g2 = []
      t = i
      for i in range(len(n)):
         if t % 2:
            g1.append(n[i])
         else:
            g2.append(n[i])
         t = t >> 1
      printe(i,g1,g2,mx)
      add = lambda x,y : x + y
      sadd = lambda x,y : x ^ y
      if reduce(sadd,g1,0) == reduce(sadd,g2,0):
         cmx = max(reduce(add,g1,0),reduce(add,g2,0))
         if (cmx>mx):
            mx = cmx
         printe(reduce(add,g1,0),reduce(add,g2,0))
         printe(reduce(sadd,g1,0),reduce(sadd,g2,0))
   if mx == -1:
      return "NO"
   else:
      return mx                
      

def simulate():
   input()
   n = [int(i) for i in input().split()]   
   return brute_force(n)         
      
      
if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{}: {}".format(i+1,simulate()))

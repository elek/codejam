#!/usr/bin/python2
import sys

from bti import BTI
from datetime import datetime
MOD = 1000000007
def solve():

   (n,m,X,Y,Z) = [int(i) for i in raw_input().split()]
   A = []
   for i in range(m):
      A.append(int(input()))
   limits = []
   for i in range(n):
      limits.append(A[i % m])
      A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z

   t = dict()
   bt = BTI(Z+1)
   a = 1
   for l in limits:
      v = l + 1         
      i = bt.readSum(v - 1)
      bt.update(v,(i+1) % MOD)
      if a % 50000 == 0:
         sys.stderr.write(str(a)+"\n")
      a+=1
   return bt.readSum(Z+1) % MOD

if __name__ == '__main__':
   for i in range(input()):
      print "Case #{0}: {1}".format(i+1,solve())

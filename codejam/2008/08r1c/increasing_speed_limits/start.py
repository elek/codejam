#!/usr/bin/python2
from datetime import datetime
MOD = 1000000007
def solve():
   print datetime.now()
   (n,m,X,Y,Z) = [int(i) for i in raw_input().split()]
   A = []
   for i in range(m):
      A.append(int(input()))
   limits = []
   for i in range(n):
      limits.append(A[i % m])
      A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z

   t = dict()
   a = 1
   for l in limits:
      su = 1
      for k,v in t.iteritems():
         if (k<l):
            su += t[k] 
      if l in t:
         t[l] = (t[l] + su) % MOD
      else:
         t[l] = su % MOD
      a += 1
      
   summ = 0
   for k,v in t.iteritems():
      summ += v
   print datetime.now()
   return summ % MOD

if __name__ == '__main__':
   for i in range(input()):
      print "Case #{0}: {1}".format(i+1,solve())

#!/usr/bin/python

def solve():
   (N,K) = map(int, raw_input().split())
   for i in xrange(N):
      if (K % 2 == 0):         
         return 'OFF'
      K >>= 1
   return 'ON'

if __name__ == '__main__':
   for i in range(input()):
      print "Case #{}: {}".format(i+1,solve())
      


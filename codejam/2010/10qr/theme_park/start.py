#!/usr/bin/python2

class simulate():
   def __init__(self,k,g):
      self.k = k
      self.g = g
      self.i = 0
   def next(self):
      tmpsum = 0
      no = 0
      while (tmpsum + self.g[self.i] <= self.k):
         tmpsum += self.g[self.i]
         self.i+=1
         no +=1
         if (self.i==len(self.g)):
            self.i=0
      return tmpsum
   

def solve():
   (R,k,N) = map(int,raw_input().split())
   g = map(int,raw_input().split())
   s = simulate(k,g)
   summa = 0
   for i in xrange(R):
      summa += s.next()
   return summa
      
if __name__ == '__main__':
   for i in range(input()):
      print "Case #{}: {}".format(i+1,solve())

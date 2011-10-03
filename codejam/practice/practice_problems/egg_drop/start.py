#!/usr/bin/python2

import math
import sys

class EggBreak:
   MAX = long(4294967296)
   cache = {}
   cacheSize = 0
   def initCache(self):      
      self.cache[1,0] = 0
      for k in xrange(1,33):
         self.cache[1,k] = 1
      for trz in xrange(2,100000000):
         self.cache[trz,0] = 0
         if (trz % 10000) == 0: sys.stderr.write(str(trz))         
         for breakz in xrange(1,33):
            if (trz==1):
               self.cache[trz,1] = 1
               continue
            self.cache[0,breakz] = 1
            key = (long(trz),long(breakz))
            keya = (long(trz-1),long(breakz-1))
            keyb = (long(trz-1),long(breakz))            
            val = self.cache[keya] + self.cache[keyb] + 1
            if self.cache[keya] == -1 or self.cache[keyb]==-1 or val>self.MAX:
               self.cache[key] = -1
            else:
#               print str(trz)+"-"+str(breakz)+" "+str(val)
               self.cache[key] = val
            if (breakz==2 and self.cache[key]==-1):
               self.cacheSize = long(trz)
               sys.stderr.write("stop caching at " + str(trz))
               return

   def getMinBreak(self,level,tryz,breakz):
      i = 1
      while i <= breakz:
         l = self.getMaxLevel(tryz,i)
         if (l==-1 or l>=level):
            return i
         i += 1
   def getMinTry(self,level,tryz,breakz):
      i = 1
      while i <= tryz:
         l = self.getMaxLevel(i,breakz)         
         if (l>=level or l==-1):
            return i
         i += 1
   def getMaxLevel(self,tryz,breakz):
      if (breakz>32):
         breakz = 32
      if (breakz == 1):
         return tryz      
      if (tryz > self.cacheSize):
         return -1   
      return self.cache[(tryz,breakz)]
      

def start():   
   e = EggBreak()
   e.initCache()
   for i in xrange(input()):
      line = raw_input().split(" ")
      a,b,c = long(line[0]),long(line[1]),long(line[2])
      l = e.getMaxLevel(b,c)
      t = e.getMinTry(a,b,c)
      b = e.getMinBreak(a,b,c)
      print("Case #"+str(i+1)+": "+str(l)+" "+str(t)+" "+str(b))

if __name__ == '__main__':
   start()


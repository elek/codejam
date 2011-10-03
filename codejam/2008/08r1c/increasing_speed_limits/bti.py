#!/usr/bin/python2

class BTI:
   
   def __init__(self, maxval):
      self.maxval = maxval
      self.values = {}

      
   def update(self, idx, val):
      while (idx < self.maxval):
         self.set(idx,self.get(idx) + val)
         idx += (idx & -idx)
   def readSum(self,idx):
      sm = 0
      while(idx>0):
         sm += self.get(idx)
         idx -= (idx & -idx)
      return sm
            
   def get(self, idx):
      if idx in self.values:
         return self.values[idx]
      return 0
         
   def set(self,idx, val):
      self.values[idx] = val
      
   
   


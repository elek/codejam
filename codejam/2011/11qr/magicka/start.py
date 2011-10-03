#!/usr/bin/python3
import math
import sys

def check(d,combs,opps):
   printe(d)
   ix = len(d)
   if (ix)==1:
      return   
   for ct in combs:
      if (ct[0]==d[ix-1] and ct[1] == d[ix-2]) or (ct[1]==d[ix-1] and ct[0] == d[ix-2]):
         d.pop()
         d.pop()
         d.append(ct[2])
         printe("replaced with " + ct[2])
         return
   for op in opps:
      if (d[ix-1] == op[0] and op[1] in d[:ix-1]) or (d[ix-1] == op[1] and op[0] in d[:ix-1]):
         while len(d)>0:
            d.pop()
         printe("clear")
         return
      
            
      
         
   
def printe(*st):
   sys.stderr.write(",".join([str(x) for x in st])+"\n")
   
def simulate():
   raw = input().split()
   ix = int(raw[0]) + 1
   combs = raw[1:ix]
   ix2 = ix + int(raw[ix]) + 1
   opps = raw[ix+1:ix2]
   queue = raw[ix2+1:][0]
   d = []
   for q in queue:
      d.append(q)
      check(d,combs,opps) 
   printe(combs,opps,queue)
   return "[" + ", ".join(d) + "]"   
         
      

      
if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{}: {}".format(i+1,simulate()))

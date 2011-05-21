#!/usr/bin/python3
import math
import sys

def printe(*st):
   sys.stderr.write(",".join([str(x) for x in st])+"\n")
   
def simulate():
   [n, pd, pg] = [int(a) for a in input().split()]
   if (pg==100 and pd<100):
      return "Broken"
   if (pg==0 and pd>0):
      return "Broken"
   if (pg==100 and pd==100):
      return "Possible"
   if (pg==0 and pd==0):
      return "Possible"
      
   for i in range(1,n+1):
      if i * pd % 100 != 0:
         continue
      for j in range(1,i+1):
         if i * pd == 100 * j:
            #print(i,j)            
            return "Possible"
   return "Broken"
      

      
if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{}: {}".format(i+1,simulate()))

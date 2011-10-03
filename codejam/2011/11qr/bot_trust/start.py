#!/usr/bin/python3
import math
import sys
def printe(*st):
   sys.stderr.write(",".join([str(x) for x in st])+"\n")
   
def simulate():
   raw = input().split()
   dests = []
   printe(raw)
   for i in range(int(raw[0])):
      dests.append(raw[1+i*2] + raw[2+i*2])
   
   # orange,blue
   pos = {'O':1,'B':1}
   time = {'O':0,'B':0}
   
   s = 0
   for dest in dests:      
      d = int(dest[1:])
      t = abs(d - pos[dest[0]]) - (s - time[dest[0]])
      if t<0:
         t = 0
      t += 1
      printe(pos,time,s,d,t,dest[0])      
      s += t
      pos[dest[0]] = d
      time[dest[0]] = s      
      
   printe(pos,time,s)
   return s     
         
         
      

      
if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{}: {}".format(i+1,simulate()))

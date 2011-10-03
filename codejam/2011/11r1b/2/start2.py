#!/usr/bin/python3
import math
import sys

def printe(*st):
   print(st)
   return True
   sys.stderr.write(",".join([str(x) for x in st])+"\n")
   
def simulate():
  [c,d] = [int(s) for s in input().split()]
  coords = []
  for j in range(c):
     coords.append([int(i) for i in input().split()])
  printe(coords)
  
  oszlop = []
  for l in coords:
     for n in range(l[1]):
        oszlop.append(l[0])
  printe(oszlop)
  
  minx = -1
  for div in range(1,len(oszlop)):
     printe("div at "+str(div))
     back = oszlop[0:div]
     forward = oszlop[div:]
     printe(back,forward)

     vback = 0     
     for l in range(1,len(back)):
        wl = d-abs(back[l]-back[l-1])
        wait = wl
        if (wl<0): wait = 0
        if (wl>d): wait = d        
        printe("bwait",wait,wl,vback)
        vback += wait
     
     vfwd = 0
     for l in range(1,len(forward)):
        wl = d-abs(forward[l]-forward[l-1])
        wait = wl
        if (wl<0): wait = 0
        if (wl>d): wait = d        
        printe("fwait",wait,wl,vfwd)
        vfwd += wait

     t0 = min(vfwd,vback)    
     t1 = max(vfwd,vback)
          
     middle = d - abs(oszlop[div] - oszlop[div-1])
     middle -= abs(t1-t0)
     printe("middle",middle)
     if (middle < 0): middle = 0
         
     res = max(vback,vfwd) + (middle /2)
     printe("result",res)     
     if minx == -1 or minx > res:
        minx = res
     printe(t0,t1,vfwd,vback,middle/2)
  if minx <0:
     return 0
  return minx
      
if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{}: {}".format(i+1,simulate()))

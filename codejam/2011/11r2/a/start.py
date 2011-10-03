#!/usr/bin/python3
import math
import sys

def printe(*st):
    return True
#   sys.stderr.write(",".join([str(x) for x in st])+"\n")

def simulate2():
   X, S, R, t, N = [int(s) for s in input().split()]
   wws = []
   x = X
   for i in range(N):
      ww = [int(s) for s in input().split()]
      s = ww[1] - ww[0]
      v = ww[2]
      wws.append((s,v))
      x -= s
   wws.append((x,0))
   wws.sort()
   st = 0
   rt = t
   for (s,v) in wws:
      print(s,v,st,rt)
      if rt > 0:
         sx = rt * (v + R)
         print("sx",sx)
         if sx >= s:
            lt = s / (v+R)
            rt -= lt
            st += t
         else:
            rt = 0
            st += sx / (v + R)
            st += (s - sx) / (v + S) 
      else:
         st+= s / (v + S)
   print(st)
      
   
def simulate():
   X, S, R, t, N = [int(s) for s in input().split()]
   wws = []
   for i in range(N):
      wws.append([int(s) for s in input().split()])
   print(X,S,R,t,wws)
   s = X / S
   print(s)
   for ww in wws:
      h = ww[1] - ww[0]            
      m =  (h / S) - (h / (S + ww[2]))
      print(ww,m)
      s -= m
   print(m)
   x = min(t * R,X) / S - min(t * R, X) / R
   print(s)
   s -= x
   
   return s      
      
if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{}:{}".format(i+1,simulate2()))

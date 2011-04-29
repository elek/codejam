#!/usr/bin/python3
import math

def add(v1,v2):
   r = []
   for i in range(len(v1)):
      r.append(v1[i] + v2[i])
   return r

def mult(v1,n):
   r = []
   for i in range(len(v1)):
      r.append(v1[i] * n)
   return r
   
def div(v1,n):
   r = []
   for i in range(len(v1)):
      r.append(v1[i] / n)
   return r
      
def process():
   v = [0,0,0]   
   c = [0,0,0]
   n = int(input())
   for i in range(n):
      l = [int(x) for x in input().split()]
      c = add(c,l[0:3])
      v = add(v,l[3:])
   
   c = div(c,n)
   v = div(v,n)
   ve = (v[0]**2+ v[1]**2+ v[2]**2) 
   if ve ==0:
      t = 0
   else:
      t = (c[0] * v[0] + c[1] * v[1] + c[2] * v[2]) / ve * -1
   if t>0:
      l = add(c,mult(v,t))
      s = math.sqrt( l[0]**2 + l[1]**2 +  l[2]**2 )
   else:
      t = 0
      s = math.sqrt( c[0]**2 + c[1]**2 +  c[2]**2 )
   return (s,t)
   
   

if __name__ == '__main__':
   for i in range(int(input())):
      p = process()
      print("Case #{0}: {1:0.8f} {2:0.8f}".format(i+1,p[0],p[1]))

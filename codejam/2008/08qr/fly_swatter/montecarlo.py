#!/usr/bin/python

import math
from random import random

def distanceFromString(coord,r,g):
   cell = g + 2 * r
   coord = abs(coord - cell * round(coord/cell))
   return coord
   
   
#distance from the origo
def distance(p):   
   return math.sqrt(p[0]*p[0]+p[1]*p[1])
   
def solve():
   [f, R, t, r, g] = [float(x) for x in raw_input().split(" ")]
   die = 0
   tryz = 0
   for i in range(10000000):      
      p = (random()*R,random()*R)
      if (p[0]<p[1]):
         continue
      if distance(p)>R:
         continue
      if not isFlyAlive(p,f,R,t,r,g):
         die += 1
      tryz += 1
   return float(die) / tryz
      
   
   
   
def isFlyAlive(point, f, R, t, r, g):
   realR = R - t - f
   if distance(point)>realR:
      return False
   if distanceFromString(point[0],r,g) < r + f:
      return False
   if distanceFromString(point[1],r,g) < r + f:
      return False
   return True


   
def main():
   for case in range(input()):
      print "Case #{0}: {1}".format(case+1,solve())

   
if __name__ == '__main__':
   main()

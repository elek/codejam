#!/usr/bin/python

import math
from random import random
 
   
#distance from the origo
def d(y,x):   
   return math.sqrt(y**2 + x ** 2)

def d2(x1,y1,x2,y2):   
   return math.sqrt((x1-x2)**2 + (y1-y2) ** 2)
   
def inters(r,coord):
   a = r ** 2 - coord ** 2  
   return math.sqrt(a)

def areaOfSegment(realR,angle):
   return realR ** 2 * angle / 2  - realR **2 /2 * math.sin(angle)

def calcAngle(x1,y1,x2,y2):
   return math.atan(y1 / x1) - math.atan(y2 / x2)
   
def area(r,t,l,b,realR):
   if d(r,t)<realR:
      return (r-l) * (t-b)
   elif (d(l,t) > realR and d(r,b)> realR):
      yi = inters(realR,l)
      xi = inters(realR,b)
      angle = calcAngle(l,yi,xi,b)     
      segment = areaOfSegment(realR,angle)
      t1 = (xi - l) * (yi-b) / 2
      return t1 + segment
   elif (d(l,t) > realR and d(r,b) <= realR):
      y1 = inters(realR,l)
      y2 = inters(realR,r)
      angle = calcAngle(l,y1,r,y2)
      rec = ((y1 - b) + (y2 - b)) * (r - l) / 2
      return areaOfSegment(realR,angle) + rec
   elif (d(l,t) <= realR and d(r,b) > realR):
      x1 = inters(realR,t)
      x2 = inters(realR,b)
      angle = calcAngle(x1,t,x2,b)            
      t1 =(x2 - l) * (t-b) / 2
      t2 = (x1 - l) * (t-b) / 2
      return areaOfSegment(realR,angle) + t1 + t2 
   elif (d(l,t) <= realR and d(r,b) <= realR):
      x1 = inters(realR,t)
      y2 = inters(realR,r)
      angle = calcAngle(x1,t,r,y2)
      t1 = (y2 - b) * (r - x1) / 2
      t2 = (t - b) * (r - x1) / 2
      r1 = (x1 - l) * (t - b)
      return areaOfSegment(realR,angle) + t1 + t2 + r1
   else:      
      print "???"
            
      
   
def solve():
   [f, R, t, r, g] = [float(x) for x in raw_input().split(" ")]
   
   if (2*f) > g:
      return 1

   realR = R - t - f
   cellSize = 2 * r + g
   
   freeArea = 0
   #calculate free rectangles bottom, left, top, right (y0,x0,y1,x1)
   (b,l,t,ri) = (r + f, r + f, r + g - f, r + g - f)
   while (True):
      if d(b,l) > realR:
         b = b + cellSize
         t = t + cellSize         
         l = r + f
         ri = r + g - f      
      if d(b,l) > realR:
         break
      a = area(ri,t,l,b,realR)
      freeArea += a
      l += cellSize
      ri += cellSize
   ra = (R * R * math.pi / 4)
   return (ra - freeArea) / ra    
      
   
   
   
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
      print "Case #{0}: {1:.6f}".format(case+1,solve())

   
if __name__ == '__main__':
   main()

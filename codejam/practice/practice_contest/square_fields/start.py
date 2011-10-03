#!/usr/bin/python2
import math

def minPoint(p1,p2):
   return (min(p1[0],p2[0]),min(p1[1],p2[1]))
def maxPoint(p1,p2):
   return (max(p1[0],p2[0]),max(p1[1],p2[1]))      
def concatenatedSize(s1,s2):
   gminp = minPoint(s1.minp,s2.minp)
   gmaxp = maxPoint(s1.maxp,s2.maxp)
   return max(gmaxp[0]-gminp[0],gmaxp[1]-gminp[1])
   
class Square:
   def __init__(self):
      self.points = []
   def addPoint(self,point):
      if len(self.points) == 0:
         self.minp = point
         self.maxp = point
      else:
         self.minp = minPoint(point,self.minp)
         self.maxp = maxPoint(point,self.maxp)
      self.points.append(point)
   def __str__(self):
      return str(self.points)
   def size(self):
      return max(self.maxp[0]-self.minp[0],self.maxp[1]-self.minp[1])   
               
   
def solve():
   def findMinimalDistance(squares):
      minIndexes = None
      minValue = -1
      for i in range(len(squares)):
         for j in range(i+1,len(squares)):
            print (i,j)
            
            value = concatenatedSize(squares[i],squares[j])
            print value
            if (minIndexes == None or value<minValue):
               minIndexes = (i,j)
               minValue = value
     # print minValue     
     # print minIndexes
      print "choosend"
      print minIndexes
      return minIndexes
      
   def combineSquares(squares,sqi1,sqi2):
      for point in squares[sqi2].points:
         squares[sqi1].addPoint(point)
      del squares[sqi2]
         
   n,k = raw_input().split()
   points = []
   for i in range(int(n)):
      pp = raw_input().split()
      points.append((int(pp[0]),int(pp[1])))
   
   squares = []
   for i in range(int(n)):
      s = Square()
      s.addPoint(points[i])
      squares.append(s)
 
   while len(squares)>int(k):
      (sqi1,sqi2) = findMinimalDistance(squares)
      combineSquares(squares,sqi1,sqi2)
      #print squares[sqi1].points
      for l in squares:
         print l.points
      
   minsize = -1
   for k in squares:           
      minsize = max(minsize,k.size())
      #print k.points
   print minsize

 

def main():
   for line in range(input()):
      print "Case #%s:"%(line+1),
      solve()

if __name__ == '__main__':
   main()

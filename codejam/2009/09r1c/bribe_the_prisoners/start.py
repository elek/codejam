#!/usr/bin/python3
import math
import sys

def printe(*st):
   sys.stderr.write(" ".join([str(i) for i in st]))
   sys.stderr.write("\n")
   
def findNonSmaller(li,n):
   for i in range(len(li)):
      if li[i]>n:
         return i
   return len(li)-1
   
   
def process():
   [p,q] = [int(i) for i in input().split()]   
   released = [int(i) for i in input().split()]
   
   released.insert(0,0)
   released.append(p+1)
   printe(p,q, released)
   resp = 0 
   
   while len(released)>2:
      mi = -1
      mv = -1
      maxvalues = []
      for i in range(1,len(released)-1):         
         v = released[i]-released[i-1] -1 + released[i+1]-released[i] - 1
         printe("i",i,v)
         if mv == -1 or v < mv:
            mv = v
            mi = i         
      resp += mv
      printe("xxx",released[mi],mi,mv, released[mi-1],released,resp)
      released.pop(mi)
   return resp
         

if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{0}: {1}".format(i+1,process()))

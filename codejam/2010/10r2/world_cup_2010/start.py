#!/usr/bin/python3
import math
def solve():
   tree = []
   p = int(input())
   groups = [int(t) for t in input().split()]
   for i in range(p):
      tree.extend([int(l) for l in input().split()])
   
   tree.reverse()
   print(tree)
   n = 2 ** p - 1
   for i in range(2 ** (p - 1)):
      l =  n - i
      t = []
      while l>0:
         t.append(l-1)
         l = int(math.floor(l/2))
      print(l,t)
      
   for a in range(p):
      for b in range(groups[a]):
         
   print(p,tree)

if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{}: {}".format(i+1,solve()))



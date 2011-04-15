#!/usr/bin/python
from functools import reduce

def check(l):
   base = l[0]
   if base == '.':
      return None
   for i in range(1,len(l)):
      if l[i] != base:
         return None
   return base
   
def same(a,b):
   return a and (b == 'R')
def process():
   [N,K] = [int(x) for x in input().split()]
   table = []
   for n in range(N):
      line  = []
      for c in input():
         if c != '.':
            line.append(c)
      while len(line) < N:
         line.insert(0,'.')
      table.append(line)
#   for x in range(N):
#      for y in range(N):
#         print(table[x][y],end="")
#      print("")
   winners = set()
   for y in range(N):
      for x in range(N-K+1):               
         s = [table[y][x+i] for i in range(K)]
         winner = check(s)         
         if (winner):
            winners.add(winner)
   
   for x in range(N):
      for y in range(N-K+1):               
         winner = check([table[y+i][x] for i in range(K)])
         if (winner):
            winners.add(winner)
   for x in range(K-1,N):
      for y in range(N-K+1):               
         winner = check([table[y+i][x-i] for i in range(K)])
         if (winner):
            winners.add(winner)
   for x in range(N-K+1):
      for y in range(N-K+1):               
         winner = check([table[y+i][x+i] for i in range(K)])
         if (winner):
            winners.add(winner)
            
   if len(winners)==2:
      return "Both"
   elif len(winners)==0:
      return "Neither"
   elif 'R' in winners:
      return "Red"
   else:
      return 'Blue'
      
   


   

   
if __name__=='__main__':
   for i in range(int(input())):
      print("Case #{0}: {1}".format(i+1,process()))

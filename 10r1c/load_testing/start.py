#!/usr/bin/python3

import math 
e = 50
rntp = []

def tnp1(l):
   if l==1:
      return 1
   else:
      return tnp1(l-1) * 2 + 1
      
rntp.append(0)      
for i in range(1,e):
   rntp.append(rntp[i-1] * 2 +1)


def rtnp1(l):
   k = 0
   while True:
      if rntp[k] >= l:
         return k
      k += 1
      if k>e:
         raise Error("ojojoj")
   

def process():
   [l, p , c] = [int(i) for i in input().split()]
   n = math.ceil(math.log(p/l,c))
   return rtnp1(n - 1) 
                   


if __name__ == '__main__':   
   for i in range(int(input())):
      print("Case #{0}: {1}".format(i+1,process()))
         
         


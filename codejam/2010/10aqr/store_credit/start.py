#!/usr/bin/python

def find_index1(lista,value):
   for i in range(len(lista)):
      if lista[i] == value:
         return i
   return None
   
def find_index2(lista,value):
   for i in range(len(lista)-1,-1,-1):
      if lista[i] == value:
         return i
   return None   

def check(orig,n,credit):
   p1 = list(orig) 
   p2 = list(p1)   
   p1.sort()
   p2.sort(reverse=True)
   i1 = 0
   i2 = 0
   while (i2<n and i1<n):
      v1 = p1[i1]
      v2 = p2[i2]
      if v1+v2 == credit and i1!=i2:
         return v1,v2
      elif (v1+v2>credit and i2<n-1):
         i2 += 1
      else:
         i1 += 1
   
def solve():
   credit = input()
   n = input()
   orig = [int(x) for x in raw_input().split()]
   v1,v2 = check(orig,n,credit)
   r = [find_index1(orig,v1)+1,find_index2(orig,v2)+1]
   r.sort()
   return r
      
if __name__ == '__main__':
   for i in range(input()):
      s = solve()
      print "Case #{}: {} {}".format(i+1,s[0],s[1])


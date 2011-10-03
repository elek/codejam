#!/usr/bin/python2

def solve():
   (p,k,l) = [int(x) for x in raw_input().split()]
   freq = [int(x) for x in raw_input().split()]
   freq.sort(reverse=True)
   
   idx = 0
   click = 0
   for i in freq:
      click += i * ((idx / k) +1)
      idx += 1
   
   return click


if __name__ == '__main__':
   for case in range(input()):
      print("Case #{0}: {1}".format(case+1,solve()))

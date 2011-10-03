#!/usr/bin/python

def solve():
   li = raw_input().split()
   return " ".join([li[i] for i in range(len(li)-1,-1,-1)])

if __name__ == '__main__':
   for i in range(input()):
      print "Case #{}: {}".format(i+1,solve())

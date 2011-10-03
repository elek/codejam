#!/usr/bin/python

def solve():
   input()
   v1 = [int(x) for x in raw_input().split()]
   v2 = [int(x) for x in raw_input().split()]
   v1.sort()
   v2.sort(reverse=True)
   s = 0
   for (x,y) in zip(v1,v2):
      s += x*y
   return s
def main():
   for case in range(input()):
      print "Case #{0}: {1}".format(case+1,solve())


if __name__ == "__main__":
   main()

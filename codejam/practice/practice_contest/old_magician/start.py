#!/usr/bin/python2

def solve():   
   w,b = raw_input().split()
   if int(b) % 2 == 0:
      print "WHITE"
   else:
      print "BLACK"

   
def start():
   for lin in range(input()):
      print "Case #%s:"%(lin+1),
      solve()

if __name__ == '__main__':
   start()

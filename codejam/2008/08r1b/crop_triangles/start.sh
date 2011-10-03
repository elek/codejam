#!/usr/bin/python2
import logging

logging.basicConfig(level=logging.ERROR)

def calc_rectangles(points):
   counter = 0
   types = {}
   for a in range(3):
      for b in range(3):
         types[(a,b)] = 0
   for point in points:
      types[(point[0] % 3, point[1] % 3)] += 1
   logging.debug(types)
   kp = types.keys()
   for a in range(9):
      for b in range(a,9):
         for c in range(b,9):
            if ((kp[a][0] + kp[b][0] + kp[c][0]) % 3) == 0:
               if ((kp[a][1] + kp[b][1] + kp[c][1]) % 3) == 0:
                  num = 1
                  prev = -1
                  decr = 1
                  logging.debug((a,b,c))
                  for pos in (a,b,c):
                     val = types[kp[pos]]
                     if (prev == pos): 
                        val -= decr
                        decr += 1
                     logging.debug((num,val))
                     num *= val
                     prev = pos
                  logging.debug(str(num))
                  if (a==b==c):
                    num /= 6
                  elif (a==b or b==c):
                    num /= 2
                  logging.debug("add {0}".format(num))
                  counter+=num   
   return counter

def solve():
   (n, A, B, C, D, x0, y0, M) = map(int,raw_input().split()) 
   X = x0
   Y = y0
   points = []
   points.append((X, Y))
   for i in range(n-1):
      X = (A * X + B) % M
      Y = (C * Y + D) % M
      points.append((X, Y))
   return calc_rectangles(points)
               

def main():
   for case in range(input()):
      print "Case #{0}: {1}".format(case+1, solve())




if __name__ == '__main__':
   main()

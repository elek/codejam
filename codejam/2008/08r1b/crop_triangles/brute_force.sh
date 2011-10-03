#!/usr/bin/python2


def calc_rectangles(points):
   counter = 0
   for a in range(len(points)):
      for b in range(a+1,len(points)):
         for c in range(b+1,len(points)):
            if ((points[a][0] + points[b][0] + points[c][0]) % 3) == 0:
               if ((points[a][1] + points[b][1] + points[c][1]) % 3) == 0:
                  counter += 1
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

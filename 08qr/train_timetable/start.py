#!/usr/bin/python

def solve():
   def findMaxRequired(l):
      m = 0
      req = 0
      for i in range(len(l)):
         act = l[i][4]         
         if (act=='d'):
            req +=1
         else:
            req -=1
         m = max(m,req)
      return m 
      
   turnaround = input()
   depFromA = []
   depFromB = []
   [na,nb] = [int(x) for x in raw_input().split()]
   for a in range(na):
      v = raw_input().split(" ")
      #train departure
      depFromA.append(convert(v[0],0)+"d")
      #lesser train required
      depFromB.append(convert(v[1],turnaround)+"a")
      
   for b in range(nb):
      v = raw_input().split(" ")
      #train departure
      depFromB.append(convert(v[0],0)+"d")
      #lesser train required
      depFromA.append(convert(v[1],turnaround)+"a")
   
   depFromA.sort()
   depFromB.sort()

   return (findMaxRequired(depFromA),findMaxRequired(depFromB))
   
   
def main():
   for case in range(input()):
      (a,b) = solve()
      print "Case #{0}: {1} {2}".format(case+1,a,b)

def convert(string,turnaround):
   [h,s] = [int(x) for x in string.split(":")]
   return "{0:04}".format(h*60+s+turnaround)
   
if __name__ == '__main__':
   main()

#!/usr/bin/python3
import math
import sys

def printe(*st):
    return True
#   sys.stderr.write(",".join([str(x) for x in st])+"\n")
   
def simulate():
   n = int(input())
   t = []
   for i in range(n):
      t.append(input())

   sms = []
   wp = []
   for i in range(n):
      sm = 0   
      db = 0
      for j in range(n):
         if t[i][j]!='.':
            db += 1
            sm += int(t[i][j])
      wp.append(sm/db)      
      sms.append(db)
      
   printe(wp)
   printe(sms)
   
   owp = []
   for i in range(n):
      owpsum = 0
      for j in range(n):
         if t[i][j] != '.':            
            l = (wp[j] * sms[j] - int(t[j][i])) / (sms[j] - 1)
            owpsum += l
            printe("x",wp[j],sms[j],t[j][i],sms[i])
            printe(i,j,l)
      g = owpsum / sms[i]
      owp.append(g)      
   printe(owp)
   
   oowp = []
   for i in range(n):
      oowppart = 0    
      for j in range(n):
         if t[i][j]!='.':
            printe("oowppart",i,j,owp[j])
            oowppart += owp[j]
      oowp.append(oowppart/sms[i])

   printe(oowp)
   printe(t)
   result = []
   for i in range(n):
      result.append(0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i])
   printe(result)
   return "\n".join([str(x) for x in result])

      
if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{}:\n{}".format(i+1,simulate()))

#!/usr/bin/python2

import logging
logging.basicConfig(level=logging.INFO)

def is_prime(n):
   for x in range(2, int(n**0.5)+1):
      if n % x == 0:
         return False
   return True
   
def solve():
   (a,b,p) = map(int,raw_input().split())
   
   numbers = {}
   for n in range(a,b+1):
      numbers[n] = n
   logging.debug(numbers)      
      
   for i in range(p,b+1):      
      if is_prime(i):
         if (a % i) == 0:
            start = a
         else:
            start = a + i - (a % i)
            
         logging.debug(numbers)
         
         mn = b
         k = start
         values = set()
         while (k<=b):
            logging.debug("check {0}".format(k))
            values.add(numbers[k])
            mn = min(mn,numbers[k])
            k += i         
         logging.debug("min {}".format(mn))
         logging.debug("group {}".format(values))
         
         k = start
         for n in range(a,b+1):
            if numbers[n] in values:
               numbers[n] = mn
   
   sets = set()
   for n,group in numbers.iteritems():
      if group not in sets:
         sets.add(group)
   return len(sets)            

if __name__ == '__main__':
   for case in range(input()):
      print "Case #{0}: {1}".format(case+1,solve())
   
      
      
      

   
   



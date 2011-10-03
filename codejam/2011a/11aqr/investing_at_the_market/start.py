#!/usr/bin/python
import math
def business(buy,sell,amount,offers):
   return math.floor(amount/offers[buy])*(offers[sell]-offers[buy])
   
def process():
   amount = int(input())         
   offers = [int(x) for x in input().split()]
   buy = None
   sell = None
   minv = None
   minl = None
   for i in range(len(offers)):
      if (buy==None):
         if offers[i]<=amount:
            buy = i
            minl = i
            minv = offers[i]
         continue
            
      if sell == None:
         sell = i
      else:
         a1 = business(buy,sell,amount,offers)
         a2 = business(minl,i,amount,offers)
         if a2>a1 or (a2==a1 and offers[minl]<offers[buy]):
            buy = minl
            sell = i         
      if offers[i]<amount and offers[i]<minv:
         minv = offers[i]
         minl = i
   if buy == None or sell == None or business(buy,sell,amount,offers)<0:
      return "IMPOSSIBLE"         
   return "{0} {1} {2}".format(buy+1,sell+1,business(buy,sell,amount,offers))
    

if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{0}: {1}".format(i+1,process()))
         
      

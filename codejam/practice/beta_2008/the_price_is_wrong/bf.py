#!/usr/bin/python

import sys
import copy


	
def calcChanges(words,prices,position,changes,lastPrice):
#      print "position "+str(position)
#      print "changes " + str(changes)
#      print "lastPrice " + str(lastPrice)
      if (position==len(words)):
         return sorted(changes)
      curr = prices[position]
      if (lastPrice>curr):
         return calcChanges(words,prices,position+1,changes + [words[position]],lastPrice)
      minPrice = 0
      for e in xrange(position+1,len(words)):
         minPrice = min(minPrice,prices[e])
      if (minPrice<curr):
         opt1 = calcChanges(words,prices,position+1,changes,curr)
         opt2 = calcChanges(words,prices,position+1,changes + [words[position]],lastPrice)
         if len(opt1)==len(opt2):
            if (opt1<opt2): return opt1
            else: return opt2
         elif len(opt1)<len(opt2):
            return opt1
         else:
            return opt2
      return calcChanges(words,prices,position+1,changes,curr)
   

def start():
	for i in range(input()):
		
		words = raw_input().split()
		prices = [int(x) for x in raw_input().split()]
		ch = calcChanges(words,prices,0,[],0)
		print "Case #"+str(i+1)+": " + (" ".join(ch))
		sys.stdout.flush()

if __name__ == '__main__':
	start()

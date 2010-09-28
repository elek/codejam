#!/usr/bin/python
import math

class EggBreak:
	MAX = 4294967296
	cache = {}
	def initCache(self):
		for trz in range(1,1000000):
			if (trz % 10000) == 0: print trz
			for breakz in range(1,33):
				key = (trz,breakz)
				keya = (trz-1,breakz-1)
				keyb = (trz-1,breakz)				
				if (trz<2):
					self.cache[key]=1
				elif (breakz ==1):
					self.cache[key]=trz
				elif (self.cache[keya]==-1 or self.cache[keyb]==-1):
					self.cache[key] = -1
				else:
					self.cache[key] = self.cache[keya] + self.cache[keyb] + 1
				if (breakz==2 and self.cache[key]>self.MAX):
					print "stop caching at " + str(trz)
					return
	def getValue(self,tryz,breakz):
	   if breakz > 32:
	      breakz = 32
	   if breakz == 1:
	      return tryz
	   return self.cache[(tryz,breakz)]
	def getMinBreak(self,level,tryz,breakz):
		i = 1
		while i <= breakz:
			l = self.getValue(tryz,i)
			if (l==-1 or l>=level):
				return i
			i += 1
	def getMinTry(self,level,tryz,breakz):
		i = 1
		while i <= tryz:
			l = self.getValue(i,breakz)			
			if (l>=level or l==-1):
				return i
			i += 1
	def getMaxLevel(self,level,tryz,breakz):
		if breakz>32:
			return -1
		l = self.cache[(tryz,breakz)]
		return l
		
		
e = EggBreak()
e.initCache()
print "cache is build"
f = open('../set/C-large-practice.in')
o = open('../set/C-large-practice.out','w+')
num = int(f.readline())
for i in range(1,num+1):
	line = f.readline().split(" ")
	l = e.getMaxLevel(int(line[0]),int(line[1]),int(line[2]))
	t = e.getMinTry(int(line[0]),int(line[1]),int(line[2]))
	b = e.getMinBreak(int(line[0]),int(line[1]),int(line[2]))
	o.write("Case #"+str(i)+": "+str(l)+" "+str(t)+" "+str(b)+"\n")

 




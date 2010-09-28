#!/usr/bin/python


class Number:
	system = '0123456789'
	value = 0	
	def __init__(self, system, value=0):
		self.system = system;
		self.value = value;
	def parse(self,str):   
		self.value = 0
		i = len(str) - 1 
		pow = 1
		while i>=0:
			self.value += self.decimalValue(str[i]) * pow
			i -= 1
			pow = pow * len(self.system)
		return self.value
	def decimalValue(self,symbol):
 		return self.system.find(symbol)
	def format(self):
		val2 = self.value
		pow = len(self.system)
		ret = ''
		while val2 > 0:
			r = val2 % pow
			ret = str(self.system[r]) + ret			
			val2 = (val2 - r)/pow
		return ret

file = 'A-large-practice.in'
f = open(file)
out = open(file + '.res','w+')
num = int(f.readline())
for i in range(num):
   line = f.readline()
   t = line.split(" ")
   orig = Number(t[1])
   orig.parse(t[0])
   out.write("Case #" + str(i+1) + ": " + Number(t[2].strip(),orig.value).format()+"\n")
   

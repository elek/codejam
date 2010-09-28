#!/usr/bin/python
import sys

class TurnLeft:
    def __init__(self):
	self.properties = {}
	self.pos = [0,0]
	self.minPos = [0,1]
	self.maxPos = [0,0]
	self.table = {}
	self.direction = 2
    def step(self,step):
	if (step=='R'):
	    self.direction += 1
	elif (step=='L'):
	    self.direction -= 1
	elif (step=='W'):
	    self.setProp(self.direction % 4)
	    self.move(self.direction)
	    self.setProp((self.direction - 2) % 4)
		
    def move(self,direction):
	if (direction % 4 == 0):
	    self.pos = (self.pos[0],self.pos[1]-1)
	elif (direction % 4 == 1):
	    self.pos = (self.pos[0]+1,self.pos[1])
	elif (direction % 4 == 2):
	    self.pos = (self.pos[0],self.pos[1]+1)
    	elif (direction % 4 == 3):
	    self.pos = (self.pos[0]-1,self.pos[1])
    def dirToBit(self,k):
	if k==0: dd = 0
	elif k==1: dd = 3
	elif k==2: dd = 1
	elif k==3: dd = 2
	return dd

    def recalcMaxMin(self):
	self.minPos[0] = min(self.minPos[0],self.pos[0])
	self.minPos[1] = min(self.minPos[1],self.pos[1])
	self.maxPos[0] = max(self.maxPos[0],self.pos[0])
	self.maxPos[1] = max(self.maxPos[1],self.pos[1])
    def do(self,pattern):
	for i in xrange(len(pattern)):
	    self.step(pattern[i])
	    if (i!=len(pattern)-1):
		self.recalcMaxMin();
    def setProp(self,direct):
	    key = (self.pos[0],self.pos[1])
	    if (not key in self.properties):
		self.properties[key] = 0
	    self.properties[key] =self.properties[key] | 1 << self.dirToBit(direct % 4)
	


	    
	
def main(pattern1,pattern2,writer):
    t = TurnLeft()
    t.do(pattern1)
    t.step('R')
    t.step('R')
    t.do(pattern2)
    for y in range(t.minPos[1],t.maxPos[1]+1):
        for x in range(t.minPos[0],t.maxPos[0]+1):
    	    key = (x,y)
    	    if key in t.properties:
    		writer.write(hex(t.properties[(x,y)])[2:])
        writer.write("\n")

def start():
    for num in xrange(input()):
	writer = sys.stdout
	writer.write("Case #"+str(num+1)+":\n");
	patterns = raw_input().split()
	main(patterns[0],patterns[1],writer)

if __name__=='__main__':
    start()
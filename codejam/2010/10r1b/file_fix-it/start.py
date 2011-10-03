#!/usr/bin/python

def readList(num):
   a = []
   for i in range(num):
      a.append(input())
   return a

class Node():
   
   def __init__(self,name,new = False):
      self.name = name
      self.child = []
      self.new = new
      
   def append(self, elemList, new = False):
      if len(elemList)==0:
         return
      for child in self.child:
         if child.name == elemList[0]:
            if len(elemList)>1:
               child.append(elemList[1:], new)
            return;
      #not found
      newNode = Node(elemList[0], new)
      self.child.append(newNode)
      newNode.append(elemList[1:], new)
   
   def print(self,level = 0):
      pad = ""
      for i in range(level):
         pad += " "
      print(pad + self.name + " "+ str(self.new))
      for c in self.child:
         c.print(level+3)
         
   def count(self):
      c = 0
      for i in self.child:
         c += i.count()
      if self.new:
         c += 1
      return c
      

def process():
   [old,new] = [int(i) for i in input().split()]
   olds = readList(old)
   news = readList(new)
   root = Node("root")
   for o in olds:
      root.append(o.split("/")[1:])
      
   for n in news:
      root.append(n.split("/")[1:], True)   
#   root.print()
   return root.count()

   


if __name__ == '__main__':   
   for i in range(int(input())):
      print("Case #{0}: {1}".format(i+1,process()))
         

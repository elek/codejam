#!/usr/bin/python2


class LinkedList:
   def __init__(self):
      self.start = None
   
   def add(self,value):
      if self.start == None:
         self.start=Node(value)
      else:
         self.findLast().link(Node(value))
         
   def findLast(self):
      prev = None
      node = self.start
      while (node!=None):
         prev = node
         node = node.next         
      return prev
   
   def get(self,index):
      node = self.start
      while (node!=None and index>0):
         node = node.next
         index-=1
      if (node==None or index>0): return None
      else: return node
      
   def __call__(self,index):
      node = self.get(index)
      if (node==None): return None
      else: return node.value
      
   def insert(self,index,value):
      p = self.get(index)
      next = p.next
      new = Node(value)
      new.link(next)
      p.next = new
      
   def __str__(self):
      node = self.start
      res = "["
      sep = ""
      while (node):
         res+= sep + str(node.value)
         node = node.next
         sep = ", "
      res += "]"
      return res
      
   def reverse(self):
      node = self.start
      p = None
      while (node):
         next = node.next
         node.next = p
         p = node
         node = next
      self.start = p
         
      
   
class Node:
   def __init__(self,value):
      self.value = value
      self.next = None
   def link(self,node):
      self.next = node
         
   

ll = LinkedList()
print str(ll)
ll.add(2)
print str(ll)
ll.add(3)
print str(ll)
print (ll(0))
ll.insert(0,-1)
print str(ll)
ll.add(5)
ll.add(7)
print str(ll)
ll.reverse()
print str(ll)


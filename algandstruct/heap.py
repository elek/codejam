#!/usr/bin/python

class heap():
   def __ini__(self):
      self.values = []
      self.size = 0
   def left(self,index):
      return index * 2
   def right(self,index):
      return index * 2 + 1
   def parent(self,index):
      return index / 2
   def __getitem__(self,index):
      return self.values[index-1]
         
   def replace(self,i1,i2):       
      tmp = self.values[i1-1]
      self.values[i1-1] = self.values[i2-1]
      self.values[i2-1] = tmp

   def init(self,values):
      self.values = values
      self.size = len(values)
      
   def restore_heap(self):
      for i in range(self.size / 2,0,-1):
         self.__heap_check(i)
         
   def __heap_check(self,index):
      left = self.left(index)
      right = self.right(index)
      
      max_index = None
      max_value = None
      for l in [left,right,index]:
         if l<=self.size and (max_value == None or self[l] > max_value):
            max_index = l
            max_value = self[l]
      if max_index != index:
         self.replace(max_index,index)
         self.__heap_check(max_index)
                        
      
   def sort(self):
      for k in range(self.size,1,-1):
         self.replace(1,k)
         self.size -= 1
         self.__heap_check(1)
   
def sort(l):
      h = heap()
      h.init(l)
      h.restore_heap()
      h.sort()
      
sort([5,1,2,3,4,5,-10,99,123])
   

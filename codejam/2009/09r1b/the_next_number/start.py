#!/usr/bin/python3

def split(st,l):
   for i in range(len(st)-1,-1,-1):
      if st[i]>l:
         return (st[i],st[0:i]+st[i+1:])
   
      
    

def process():
   l = input()
   value = False
   end = ''
   st = l
   for i in range(len(l)-1,0,-1):
      if l[i] == '0':
         if value:
            t = "".join(sorted(st[i+1:]))
#            print(t,st[i],l[0:i] , t[0] ,'0' ,t[1:] , end)
            return l[0:i] + t[0] + '0' + t[1:] + end 
         else:
            end += '0'
            st = l[0:i]
            continue
      value = True
      if l[i-1]<l[i]:
         f,g = split(l[i:],l[i-1])
         a = g + l[i-1]
         t = "".join(sorted(a))
#         print(t)
         return l[0:i-1] + f + t
         
   n = l.count('0') + 1
   t = "".join(sorted(st))
#   print(n,t)
   return t[0] + "".join(['0' for i in range(n)]) + t[1:] 
   print(l)
   


if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{0}: {1}".format(i+1,process()))

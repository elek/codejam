#!/usr/bin/python

def insertsort(llist):
   for i in range(1,len(llist)):
      for j in range(0,i):
         if llist[i]<llist[j]:
            p = llist[j]
            llist[j] = llist[i]
            for x in range(j+1,i+1):
               t = llist[x]
               llist[x] = p
               p = t
            break      
   return llist      

def mergesort(llist,fr=0,to=-1):
   if (to==-1): to = len(llist)
   if (fr==to-1):
      return [llist[fr]]
   n = fr + (to - fr)/2
   a = mergesort(llist,fr,n)
   b = mergesort(llist,n,to)
   ai = 0
   bi = 0
   res = []
   while (ai<len(a) or bi < len(b)):
      if (ai==len(a)):
         res.append(b[bi])
         bi += 1
      elif bi==len(b):
         res.append(a[ai])
         ai += 1
      else:
         if a[ai]<b[bi]:
            res.append(a[ai])
            ai+=1
         else:
            res.append(b[bi])
            bi+=1
   return res      
   
a = [11,100,1,9,3,4,3]
insertsort(a)
print a
#print insertsort(range(100,0,-1)) 

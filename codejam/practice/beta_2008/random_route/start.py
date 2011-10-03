#!/usr/bin/python



def solve():
   
   def findNext(cities,dest):
      minCity = None
      minTime = -1      
      for city in cities:
         time = dest[city]
         if (time==None):
            continue
         if (minCity == None or time < minTime):
            minTime = time
            minCity = city
      return minCity 


   
   
   
   roads = {}
   roads_by_start = {}
   roads_by_end = {}
   poss = {}
   possibleNumberOfRoutes = {}
   
  
   def addPossibilities(c,val,mult):
      if c == None:
         return

      xcities = {}
      for rid in c:
         
         start,_,_ = roads[rid]
         if start in xcities:
            xcities[start] = xcities[start] + [rid]
         else:
            xcities[start] = [rid]

      for city,rids in xcities.iteritems():
         pos = float(val) * possibleNumberOfRoutes[city] * mult         
      
         for rid in rids:
            if rid in poss:
               poss[rid] += pos
            else:
               poss[rid] = pos
         addPossibilities(prev[city],val,mult * len(rids))
      

   #read and parse input parameters
   num, start = raw_input().split()
   for id in range(int(num)):
      begin,end,time = raw_input().split()
      time = int(time)
      roads[id] = (begin,end,time)
      poss[id] = 0
      if not begin in roads_by_start:
         roads_by_start[begin] = []
      roads_by_start[begin].append(id)  
   
   cities = []
   for key,road in roads.iteritems():
      cities.append(road[0])
      cities.append(road[1])
   cities = set(cities)
   
   prev = {} 
   dist = {}   
   possibleNumberOfRoutes[start]=1
   for city in cities:
      dist[city] = None
      prev[city] = []

   noOfCities = len(cities)
   dist[start] = 0
   prev[start] = None
  
   while True:            
      nextCity = findNext(cities,dist)
      if nextCity == None:
         break                  
      
      #calculate possible number of routes for possibility calculating
      if nextCity!=start:
         noOfRoutes = 0
         for pr in prev[nextCity]:
            st,_,_ = roads[pr]
            noOfRoutes += possibleNumberOfRoutes[st]
         possibleNumberOfRoutes[nextCity] = noOfRoutes
      

      addPossibilities(prev[nextCity],float(1)/possibleNumberOfRoutes[nextCity],1)
         
      cities = cities - set([nextCity])      
      if nextCity in roads_by_start:
         for rid in roads_by_start[nextCity]:
            alt = dist[nextCity] + roads[rid][2]
            endCity = roads[rid][1]
            if (dist[endCity]==None or dist[endCity]>alt):
               dist[endCity] = alt
               prev[endCity] = [rid]
            elif (dist[endCity]==alt):
               prev[endCity].append(rid)
   
   for k,v in poss.iteritems():
      val = v / (noOfCities-len(cities)-1)
      print "%0.7f"%val,
   print 
def main():
   for case in range(input()):
      print "Case #%s:"%(case+1),
      solve()
   
   
if __name__=='__main__':
   main()

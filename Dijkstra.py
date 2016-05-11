#http://code.activestate.com/recipes/119466-dijkstras-algorithm-for-shortest-paths/

import graph
import sys


def shortestpath(time_graph, departure, destination, visited=[], distances={}, predecessors={}):
   if departure==destination:
      path=[]
      while destination!=None:
         path.append(destination)
         destination=predecessors.get(destination,None)
      return distances[departure], path[::-1]
   if not visited:
      distances[departure]=0
   for neighbor in time_graph[departure]:
      if neighbor not in visited:
         neighbordist = distances.get(neighbor, sys.maxsize)
         tentativedist = distances[departure]+time_graph[departure][neighbor]
         if tentativedist<neighbordist:
            distances[neighbor]=tentativedist
            predecessors[neighbor]=departure
            
   visited.append(departure)
   unvisiteds = dict((k,distances.get(k,sys.maxsize)) for k in time_graph if k not in visited)
   
   closestnode = min(unvisiteds, key=unvisiteds.get)
   return shortestpath(time_graph, closestnode, destination, visited, distances, predecessors)
      
def dijkstra_path(time_graph, departure, destination,visited=[], distances={}, predecessors={}):
    return shortestpath(time_graph, departure, destination,visited=[], distances={}, predecessors={})[1]
    
def dijkstra_path_time(time_graph, departure, destination,visited=[], distances={}, predecessors={}):
    return shortestpath(time_graph, departure, destination,visited=[], distances={}, predecessors={})[0]
    

      
      
#if __name__ == "__main__":
            
    
#   import excelParser
#   time_g = excelParser.createTimeGraph()
       #time_graph = graph.Graph(time_g)
    
   
   #  print (dijkstra_path(time_g, "남춘천", "포항"))
   # print (shortestpath(time_g,"청평","수원",[],{},{}))

    # print (dijkstra_path(time_g,"청평","남춘천"))
#   print (shortestpath(time_g,"서울","포항",[],{},{}))
    





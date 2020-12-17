from helpers import Map, load_map, show_map
import math
import heapq

def cal_distance(M, start, goal):
    length = M.intersections[goal][0] - M.intersections[start][0]
    width = M.intersections[goal][1] - M.intersections[start][1]
    distance = math.hypot(length, width)
    return distance

## Reference: https://en.wikipedia.org/wiki/A*_search_algorithm 

def best_path(cameFrom,current):
    print("best path called")
    
    output_path = [current]
    
    while current in cameFrom.keys():
        current = cameFrom[current]
        output_path.append(current)

    output_path.reverse()
    print(output_path)
    return output_path

def shortest_path(M, start, goal):
    print("shortest path called")
    
    openSet = set([start])
    closeSet = set()
    cameFrom = {}
    adjacents = M.intersections.keys()

    gScore = {node:float("inf") for node in adjacents}
    gScore[start] = 0
    #print(gScore)

    fScore = {node:float("inf") for node in adjacents}
    fScore[start] = cal_distance(M,start,goal)
    #print(fScore)
    
    frontier = [(fScore[start], start)]
    
    while openSet:
        
        point = heapq.heappop(frontier)[1]
        #print(point)
        
        if goal == point:
            output = best_path(cameFrom, point)
            return output
        
        if point in openSet:
            openSet.remove(point)
            closeSet.add(point)
            
        #print(M.roads[point])
        for node in M.roads[point]:
            
            if node not in openSet:
                openSet.add(node)
            
            if node in closeSet:
                continue
                
            tentative_g = gScore[point] + cal_distance(M, point, node)
            if tentative_g < gScore[node]:
                cameFrom[node] = point
                gScore[node] = tentative_g
                fScore[node] = tentative_g + cal_distance(M, node, goal)
                
                heapq.heappush(frontier, (fScore[node], node))
                
            #print(closeSet)
            #print(fScore)
    
    return ("{} is not connected to {}".format(goal,start))
    
'''Program which utilizes Dijkstra's algorithm to determine the shortest path from one node to another.'''

my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''):
    unvisited = list(graph)         #creating a list of unvisited nodes (every key in the my_graph dictionary
    distances = {node: 0 if node == start else float('inf') for node in graph}          #setting all the distances from starting node to infinity except to the starting node itself, which is set 0
    paths = {node: [] for node in graph}            
    paths[start].append(start)              #creating a path dictionary containing nodes as key and list as the key's value
    
    while unvisited:            #While there are unvisited nodes
        current = min(unvisited, key=distances.get)         #assigning current node to the node which is unvisited and has the minimun distance from the starting node
        for node, distance in graph[current]:           #for every node accessible from the current node, accessing node name and distance from the current node
            if distance + distances[current] < distances[node]:         #if (distance to target node from current node + distance to current node from starting node) < (stored distance to neighbouring node from starting node)
                distances[node] = distance + distances[current]         #assigning new value to distance from starting node to neighbouring node
                if paths[node] and paths[node][-1] == node:         #if paths to the neighboring node exists and the final node in the path is neighburing node,
                    paths[node] = paths[current][:]             #change the path to current path, using slice notation so that we create a copy of list instead of pointing paths[node] 
                else:
                    paths[node].extend(paths[current])      #if the path doesn't exist ,just add the current path to the current node to the paths.
                paths[node].append(node)                    #at the end, add the neighbouring node.
        unvisited.remove(current)               #remove the current node from unvisited nodes.
    
    targets_to_print = [target] if target else graph        #if target nodes exists then targets to print is just a list containing target node, else it's graph
    for node in targets_to_print:           #for every target node print the path
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'A', 'F')
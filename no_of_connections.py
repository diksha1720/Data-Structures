# There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.

# Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1. 

 



class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n>len(connections)+1:
            return -1
        total=0
        visited=set()
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for neighbour in neighbours[node]:
                    dfs(neighbour)
        neighbours=defaultdict(list)
        for u,v in connections:
            neighbours[u].append(v)
            neighbours[v].append(u)
            
        for i in range(n):
            if i not in visited:
                total+=1
                dfs(i)
        return total-1
        
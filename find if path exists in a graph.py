# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex start to vertex end.

# Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.

 

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if not edges or start == end:
            return True
        visited=set()
        queue=[start]
        while(queue):
            node=queue.pop(0)
            if node in visited:
                continue
            if node==end:
                return True
            visited.add(node)
            for path in edges:
                if path[0]==node:
                    queue.append(path[1])
                elif path[1]==node:
                    queue.append(path[0])  
        return False

        
        
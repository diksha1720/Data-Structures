# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False]*len(isConnected)
        def dfs(graph, curr, visited):
            visited[curr] = True
            for index, neighbor in enumerate(graph[curr]):
                if visited[index] is False and index != curr and neighbor == 1:
                    dfs(graph, index, visited)
        
        count = 0
        for i in range(len(isConnected)):
            if visited[i] is False:
                dfs(isConnected, i, visited)
                count += 1
        
        return count
        
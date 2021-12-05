# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.



class Solution:
        visited = {}
        col_stones = collections.defaultdict(list)
        row_stones = collections.defaultdict(list)
        count = 0
    
        def removeStones(self, stones: List[List[int]]) -> int:
        
        
            for s in stones:
                self.visited[(s[0], s[1])] = False
                self.col_stones[s[0]].append(s)
                self.row_stones[s[1]].append(s)
        
        
            for s in stones:
                if not self.visited[(s[0], s[1])]:
                    self.dfs(s)
            return self.count
    
        def dfs(self,st):
            self.visited[(st[0], st[1])] = True
            for c in self.col_stones[st[0]]:
                if not self.visited[c[0], c[1]]:
                    self.dfs(c)
                    self.count += 1
            for r in self.row_stones[st[1]]:
                if not self.visited[r[0], r[1]]:
                    self.dfs(r)
                    self.count += 1
        
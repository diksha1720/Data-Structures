# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.





class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[0]*len(rooms)
        visited[0]+=1
        stack=[]
        stack.extend(rooms[0])
        while(stack):
            node=stack.pop()
            if visited[node]!=0:
                continue
            visited[node]+=1
            stack.extend(rooms[node])
        for i in range(len(visited)):
            if visited[i]==0:
                return False
        return True
            
            
        
        
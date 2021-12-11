# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen=set()
        for i,ch in enumerate(s):
            if ch not in seen and s.count(ch)==1:
                return i
            seen.add(ch)
        return -1
    
    
        # unique=[]
        # repeat=[]
        # for char in s:
        #     if char not in unique and char not in repeat:
        #         unique.append(char)
        #     elif char in unique:
        #         unique.remove(char)
        #         repeat.append(char)
        # if len(unique)==0:
        #     return -1
        # return s.index(unique[0]) 
        
        
       
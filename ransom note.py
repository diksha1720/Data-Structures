# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if ch not in magazine:
                return False
            magazine=magazine.replace(ch,'',1)
        return True
        
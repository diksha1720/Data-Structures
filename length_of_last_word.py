class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        temp=list(s.split(" "))
        print(temp)
        for word in temp[::-1]:
            if word!='':
                return len(word)    
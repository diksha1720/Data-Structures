# The power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Given a string s, return the power of s.


class Solution:
    def maxPower(self, s: str) -> int:
        # maxlength=1
        # for i in range(0,len(s)-1):
        #     if s[i]==s[i+1]:
        #         k=i
        #         length=0
        #         while k<len(s) and s[k]==s[i]:
        #             length+=1
        #             k+=1
        #         maxlength=max(length,maxlength)
        # return maxlength
        maxlength=1
        length=0
        prev='#'
        for ch in s:
            if prev==ch:
                length+=1
                maxlength=max(length,maxlength)
            else:
                prev=ch
                length=1
        return maxlength
                    
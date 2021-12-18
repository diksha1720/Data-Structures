# Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

# Return the number of positive integers that can be generated that are less than or equal to a given integer n.

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        
        
        abhi = defaultdict(int)
        for i in digits:
            abhi[int(i)]=1
        
        def getlist(x):
            ans=[]
            while x:
                ans.append(x%10)
                x//=10
            return ans[::-1]
        
        def getans(index, tight, prefix):
            if index == len(numlist):
             
                return 1
            
            if dp[index][tight][prefix] !=-1 and tight !=1:
                return dp[index][tight][prefix]
            
            if tight:
                k = numlist[index]
            else:
                k = 9
            ret = 0
            
            for i in range(k+1):
                newtight = 0
                
                if i== numlist[index]:
                    newtight = tight
                    
                if abhi[i]==1 :
                    ret+= getans(index+1, newtight  ,0)
                else:
                    if i==0 and prefix:
                        ret+= getans(index+1, newtight, prefix)
                

            if not tight:
                dp[index][tight][prefix] = ret
            return ret
        
        numlist = getlist(n)
        print(numlist)
        dp=[[[-1 for i in range(2)]   for j in range(2)] for k in range(20)]
        
        return getans(0,1,1)-1
        
        
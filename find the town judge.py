# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # judge=-1
        # trusting=set()
        # for edge in trust:
        #     trusting.add(edge[0])
        # for i in range(1,n+1):
        #     if i not in trusting:
        #         judge=i
        #         for j in range(1,n+1):
        #             if j==i:
        #                 continue
        #             else:
        #                 if [j,i] not in trust:
        #                     judge=-1
        #                     break
        #         break
        #     else:
        #         continue
        # return judge
        count = [0] * (n + 1)
        
        for t in trust:
            count[t[0]] -= 1
            count[t[1]] += 1
        
        for i in range(1, n + 1):
            if count[i] == n - 1:
                return i
        
        return -1
  
class Solution:
    def fib(self, n: int) -> int:
        qb=[0]*(n+1)
        def recurMemo(n,qb):
            if n==0 or n==1:
                return n
            if qb[n]!=0:
                return qb[n]
            f1=recurMemo(n-1,qb)
            f2=recurMemo(n-2,qb)
            fn=f1+f2
            qb[n]=fn
            return fn
        return recurMemo(n,qb)
            
        
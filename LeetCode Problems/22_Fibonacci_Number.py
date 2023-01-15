class Solution:
    def fib(self, n: int) -> int:
        a,b,c=0,1,0
        if n==0 or n==1:
            return n
        
        for i in range(n-1):
            c=a+b
            a,b=b,c
        return c
    

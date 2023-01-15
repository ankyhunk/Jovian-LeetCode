class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum=n
        k=0
        
        for i in range(1,n+1):
            sum-=i
            if sum<0:
                break
            k+=1
        return k

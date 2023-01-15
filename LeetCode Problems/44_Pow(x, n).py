class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow=1.0
        if n == 0 or x==pow:
            pass
        elif n>0 :
            for i in range(n):
                pow *= x
        elif n<0 :
            for i in range(-n):
                pow *= 1/x
            
        return pow

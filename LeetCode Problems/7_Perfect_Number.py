class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        perfect=[]
        for i in range(1,int(num**0.5)+1):
            if num%i==0:
                perfect.append(i)
                if i**2!=num:
                    perfect.append(num//i)
                    print(perfect)
        return sum(perfect)==num*2

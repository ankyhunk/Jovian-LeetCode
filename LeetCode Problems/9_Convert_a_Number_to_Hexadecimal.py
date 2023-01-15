class Solution:
    def toHex(self, num: int) -> str:
        d={0:'0',1:'1',2:'2',3:'3',
           4:'4',5:'5',6:'6',7:'7',
           8:'8',9:'9',10:'a',11:'b',
           12:'c',13:'d',14:'e',15:'f'}

        num+=2**32*(num<0)
        if num==0:
            return '0'
        hex=''
        while num>0:
            rem=num%16
            hex=d[rem]+hex
            num//=16
        return hex   

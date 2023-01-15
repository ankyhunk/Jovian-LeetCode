class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if (num1=='0') or (num2=='0'):
            return '0'
        
        first = num1[::-1]
        second= num2[::-1]
        
        results=[]
        for index,digit in enumerate(second):
            results.append(self.product(digit,index,first))
        
        answer=self.sum(results)
        
        return ''.join(str(digit) for digit in reversed(answer))
    
    def product(self, digit2: str, num_zeros:int, first:List[str]) -> List[int]:
        current = [0]*num_zeros
        carry=0
        
        for digit1 in first:
            mul = int(digit1)*int(digit2)+carry
            carry = mul//10
            current.append(mul%10)
        
        if carry !=0:
            current.append(carry)
        return current
    
    def sum(self,results:List[List[int]]) -> List[int]:
        answer = results.pop()
        
        for result in results:
            new_answer=[]
            carry=0
            
            for digit1,digit2 in zip_longest(result,answer,fillvalue=0):
                curr_sum = digit1+digit2+carry
                carry = curr_sum//10
                new_answer.append(curr_sum%10)
                
            if carry!=0:
                new_answer.append(carry)
            
            answer=new_answer
        return answer

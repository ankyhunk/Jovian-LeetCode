class Solution:
    def isValid(self, s: str) -> bool:
        bracket = dict(('()','{}','[]'))
        print(bracket)
        par=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                par.append(i)
            elif len(par)==0 or i!=bracket[par.pop()]:
                return False
        return len(par)==0

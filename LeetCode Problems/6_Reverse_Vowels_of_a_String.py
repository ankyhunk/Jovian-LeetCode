class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c):
            if c in 'AEIOUaeiou':
                return True
            return False

        j=0
        list_s=[0]*len(s)
        s=list(s)

        for i in range(len(s)):
            if isVowel(s[i]):
                list_s[j]=s[i]
                j+=1
            
        for i in range(len(s)):
            if isVowel(s[i]):
                j-=1
                s[i]=list_s[j]

        return ''.join(s)

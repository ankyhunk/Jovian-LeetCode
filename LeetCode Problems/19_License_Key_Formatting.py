class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        count=0
        ans=""

        for i in reversed(range(len(s))):
            if s[i]!='-':
                ans+=s[i].upper()
                count+=1
                if count==k:
                    ans+='-'
                    count=0
        if len(ans)>0 and ans[-1]=='-':
            ans=ans[:-1]
        
        return "".join(ans[::-1])

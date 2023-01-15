class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        if s=="":
            return True
        for i in s:
            if i.isalnum():
                print(i)
                ans+=i
      
        return ans.lower()==ans[::-1].lower()

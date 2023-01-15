class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s=collections.Counter(s)
        dict_t=collections.Counter(t)
        if dict_s==dict_t:
            return True

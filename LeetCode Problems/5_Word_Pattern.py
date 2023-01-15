class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        di_pat={}
        s_li=s.split()
        if len(pattern)!=len(s_li):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in di_pat:
                if s_li[i] in di_pat.values():
                    return False
                di_pat[pattern[i]]=s_li[i]
            else:
                if di_pat[pattern[i]]!=s_li[i]:
                    return False
        return True

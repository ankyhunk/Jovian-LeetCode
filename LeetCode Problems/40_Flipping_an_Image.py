class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in image:
            ans.append(i[::-1])
        for i in ans:
            for j in range(len(i)):
                i[j]=i[j]^1
        return ans

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[]
        for i in range(numRows):
            temp=[]
            for j in range(i+1):
                if (j==0)or(j==i):
                    temp.append(1)
                else:
                    temp.append(pascal[i-1][j-1]+pascal[i-1][j])
            pascal.append(temp)
        return pascal

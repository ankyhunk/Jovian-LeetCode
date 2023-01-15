class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        flatten = []
        new_mat = []

        for row in mat:
            for col in row:
                flatten.append(col)
        #print(flatten) 
        if r*c!=len(flatten):
            return mat
        else:
            for row_index in range(r):
                new_mat.append(flatten[row_index*c:row_index*c+c])
            return new_mat

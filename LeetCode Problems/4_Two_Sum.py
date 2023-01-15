class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,n in enumerate(nums):
            print(i,n)
            m=target-n
            if m in d:
                return [d[m],i]
            else:
                d[n]=i

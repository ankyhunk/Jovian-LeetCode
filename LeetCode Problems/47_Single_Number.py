class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_nums=collections.Counter(nums)
        print(dict_nums)
        for i in dict_nums:
            if dict_nums[i]==1:
                val=i
        return val

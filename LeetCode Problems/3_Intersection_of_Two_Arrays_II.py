class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            return self.intersect(nums2,nums1)
        nums_dict=Counter(nums1)
        ans=[]
        for x in nums2:
            if nums_dict[x]>0:
                ans.append(x)
                nums_dict[x]-=1
        return ans

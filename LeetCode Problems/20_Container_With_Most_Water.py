class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        area=0
        while l<r:
            area=max(area,(r-l)*min(height[l],height[r]))
            print(l,r,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # ar = 0
        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):
        #         a = min(heights[i], heights[j]) * (j-i)
        #         ar = max(a, ar)
        # return ar
        marea = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            ar = min(heights[l], heights[r]) * (r-l)
            marea = max(marea,ar)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return marea
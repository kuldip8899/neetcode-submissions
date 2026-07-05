class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = height[0]
        l = []
        for i in range(len(height)):
            if height[i] > maxleft:
                l.append(height[i])
                maxleft = height[i]
            else:
                l.append(maxleft)
        maxright = height[-1]
        r = []
        for i in range(len(height)-1,-1,-1):
            if height[i] > maxright:
                r.append(height[i])
                maxright = height[i]
            else:
                r.append(maxright)
        r = r[::-1]
        total = 0
        for i in range(len(height)):
            total += min(l[i],r[i]) - height[i]
        return total

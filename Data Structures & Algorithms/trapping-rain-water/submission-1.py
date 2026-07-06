class Solution:
    def trap(self, height: List[int]) -> int:
        # maxleft = height[0]
        # l = []
        # for i in range(len(height)):
        #     if height[i] > maxleft:
        #         l.append(height[i])
        #         maxleft = height[i]
        #     else:
        #         l.append(maxleft)
        # maxright = height[-1]
        # r = []
        # for i in range(len(height)-1,-1,-1):
        #     if height[i] > maxright:
        #         r.append(height[i])
        #         maxright = height[i]
        #     else:
        #         r.append(maxright)
        # r = r[::-1]
        # total = 0
        # for i in range(len(height)):
        #     total += min(l[i],r[i]) - height[i]
        # return total

        l = 0
        r = len(height) - 1
        count = 0

        leftmax = 0
        rightmax = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= leftmax:
                    leftmax = height[l]
                else:
                    count += leftmax - height[l]
                l += 1
            else:
                if height[r] >= rightmax:
                    rightmax = height[r]
                else:
                    count += rightmax - height[r]
                r -= 1
        return count 
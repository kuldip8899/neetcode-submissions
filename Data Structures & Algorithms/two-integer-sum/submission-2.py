class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        seen = {}
        for i in range(len(nums)):
            a = target - nums[i]

            if a in seen:
                return [seen[a], i]

            seen[nums[i]] = i
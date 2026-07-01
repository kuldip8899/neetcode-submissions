class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # a = set(nums)
        # return len(a) != len(nums)
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen[nums[i]] = i
        return False
        
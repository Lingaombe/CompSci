class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        diff = 0
        for i in range(len(nums)):
            if i+1 < len(nums):
                if nums[i+1] - nums[i] > diff:
                    diff = nums[i+1] - nums[i]
        return diff
        
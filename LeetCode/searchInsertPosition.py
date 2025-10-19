class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        for n in nums:
            if n>target:
                return nums.index(n)
            if target>nums[-1]:
                return len(nums)
        
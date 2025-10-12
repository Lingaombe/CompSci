class Solution(object):
    def findPeakElement(self, nums):
        l = len(nums)

        for i in range(l):
            left = True
            right = True

            if i>0 and nums[i]<=nums[i-1]:
                left = False

            if i<l-1 and nums[i]<=nums[i+1]:
                right = False

            if left and right:
                return i

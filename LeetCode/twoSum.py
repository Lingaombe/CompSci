class Solution(object):
    def twoSum(self, nums, target):
        sum = 0
        l=len(nums)
        for i in range(l):
            sum = nums[i]
            ind1 = i
            for j in range(i+1, l):
                sum += nums[j]
                ind2 = j
                if sum == target:
                    li = [ind1, ind2]
                    return li
                else:
                    sum -= nums[j]
                    ind2 = 0

        
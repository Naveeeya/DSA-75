class Solution(object):
    def longestConsecutive(self, nums):
        
        if not nums:
            return 0

        count = 1
        longest = 1
        nums.sort()
        n = len(nums)

        for i in range(n-1, -1, -1):
            if nums[i] - nums[i-1] == 0:
                continue
            elif nums[i] - nums[i-1] == 1:
                count += 1
                longest = max(longest, count)
            else:
                count = 1

        return longest
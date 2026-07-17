from typing import List

nums = [-1, 0, 1, 2, 3]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output
        


# ---------------- TEST CASE ---------------- #



solution = Solution()
print(solution.productExceptSelf(nums))
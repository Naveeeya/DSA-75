from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_area = 0
        
        while left < right:
            # The area is limited by the shorter line
            current_height = min(heights[left], heights[right])
            current_width = right - left
            current_area = current_height * current_width
            
            # Update max_area if the current one is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer that points to the shorter line inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_area






heights=[1,7,2,5,12,3,500,500,7,8,4,7,3,6]

solution = Solution()
print(solution.maxArea(heights))
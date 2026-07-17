from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)

        sorted_items= sorted(
            count.items(),
            key= lambda x:x[1],
            reverse=True
        )
        
        result= []
        for num, freq in sorted_items[:k]:
            result.append(num)

        return result
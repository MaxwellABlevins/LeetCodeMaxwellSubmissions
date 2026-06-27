class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        seen = {}

        for idx, value in enumerate(nums):
            look = target - value
            if look in seen:
                return [seen[look], idx]

            seen[value] = idx


            
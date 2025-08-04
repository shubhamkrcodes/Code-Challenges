class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        non_zero_index = 0
        for i in range (n):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        
        for i in range (non_zero_index , n):
            nums[i] = 0
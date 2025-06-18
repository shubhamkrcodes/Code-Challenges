class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        n = len(nums)
        for i in range (0,n,3):
            if i + 2 < n:
                a = nums[i]
                b= nums[i+1]
                c = nums[i+2]

                if c - a > k :
                    return []
                result.append([a,b,c])
        return result
                
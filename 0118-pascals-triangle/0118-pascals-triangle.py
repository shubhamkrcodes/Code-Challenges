class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for row_num in range(numRows):
            row = [1] * (row_num + 1)  # Initialized each row with 1s 
            for j in range(1, row_num):
                # NOTE TO ME : Each interior element is the sum of the two elements above it
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)
        return triangle
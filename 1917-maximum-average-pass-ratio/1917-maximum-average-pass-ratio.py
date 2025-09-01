import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """

        # Function to calculate gain of adding one student
        def gain(p, t):
            return (p + 1) / float(t + 1) - p / float(t)

        # Max heap: Python heapq is min-heap, so we store -gain
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        # Assign each extra student
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Compute final average
        total = 0.0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p / float(t)

        return total / len(classes)

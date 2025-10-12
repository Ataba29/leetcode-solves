from typing import List
import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries_with_index = sorted([(q, i) for i, q in enumerate(queries)])

        res = [-1] * len(queries)
        min_heap = []  # heap of (interval_size, interval_end)
        j = 0

        for q, idx in queries_with_index:
            # Add all intervals that start <= query
            while j < len(intervals) and intervals[j][0] <= q:
                start, end = intervals[j]
                heapq.heappush(min_heap, (end - start + 1, end))
                j += 1

            # Remove intervals that end < query
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # Top of heap is the smallest interval covering the query
            if min_heap:
                res[idx] = min_heap[0][0]

        return res

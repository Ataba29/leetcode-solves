from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        x = Counter(nums)
        heap = []
        for num, freq in x.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
            print(heap)
        return [num for freq, num in heap]

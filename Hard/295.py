import heapq


class MedianFinder:

    def __init__(self):
        self.minHeap = []  # holds larger half
        self.maxHeap = []  # holds smaller half (as negatives)

    def addNum(self, num: int) -> None:
        # always push to maxHeap first (invert sign)
        heapq.heappush(self.maxHeap, -num)

        # move largest from maxHeap to minHeap to maintain order
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        # balance heaps
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        return (self.minHeap[0] - self.maxHeap[0]) / 2.0

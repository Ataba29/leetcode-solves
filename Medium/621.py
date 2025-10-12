import heapq
from collections import deque, Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq_map = Counter(tasks)
        max_heap = [(-cnt) for cnt in freq_map.values()]
        heapq.heapify(max_heap)
        t = 0
        q = deque()

        while max_heap or q:
            t += 1

            if max_heap:
                cnt = heapq.heappop(max_heap)
                cnt += 1
                if cnt != 0:
                    q.append((t + n, cnt))

            if q and q[0][0] == t:
                heapq.heappush(max_heap, (q.popleft()[1]))

        return t

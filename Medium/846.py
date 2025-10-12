from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False  # total cards must be divisible by group size

        count = Counter(hand)
        for card in sorted(count):  # go through sorted unique cards
            while count[card] > 0:
                for i in range(groupSize):
                    if count[card + i] <= 0:
                        return False
                    count[card + i] -= 1
        return True

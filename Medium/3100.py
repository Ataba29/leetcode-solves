class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        full = 0
        empty = numBottles

        while empty >= numExchange or full > 0:
            if empty >= numExchange:
                full += 1
                empty -= numExchange
                numExchange += 1
                continue
            res += full
            empty += full
            full = 0

        return res

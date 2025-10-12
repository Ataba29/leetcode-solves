class TimeMap:

    def __init__(self):
        self.time_dect = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dect:
            self.time_dect[key] = []
        self.time_dect[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.time_dect.get(key, [])
        if not vals:
            return ""

        l, r = 0, len(vals) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            ts, val = vals[mid]

            if ts == timestamp:
                return val
            elif ts < timestamp:
                res = val
                l = mid + 1
            else:
                r = mid - 1

        return res

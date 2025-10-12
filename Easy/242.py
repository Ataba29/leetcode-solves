class Solution(object):
    def isAnagram(self, s, t):
        x = Counter(s)
        t = Counter(t)

        return x == t

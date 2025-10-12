class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapp1 = {}
        mapp2 = {}
        sList = s.split()
        for i in range(len(pattern)):
            if sList[i] in mapp2 and mapp2[sList[i]] != pattern[i]:
                return False
            if pattern[i] in mapp1 and mapp1[pattern[i]] != sList[i]:
                return False
            mapp1[pattern[i]] = sList[i]
            mapp2[sList[i]] = pattern[i]
        return True

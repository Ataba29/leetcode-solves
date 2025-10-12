from collections import Counter, defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        res_dic = defaultdict(list)

        for strr in strs:
            rep = "".join(sorted(strr))
            res_dic[rep].append(strr)

        return res_dic.values()

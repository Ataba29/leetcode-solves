def binary_search_next(lst, prev):
    l, r = 0, len(lst) - 1
    ans = None
    while l <= r:
        mid = (l + r) // 2
        if lst[mid] > prev:
            ans = lst[mid]
            r = mid - 1
        else:
            l = mid + 1
    return ans


def Solve(s, words):
    pos = {}
    for i, ch in enumerate(s):
        pos.setdefault(ch, []).append(i)

    res = 0
    for w in words:
        prev = -1
        found = True
        for ch in w:
            if ch not in pos:
                found = False
                break
            nxt = binary_search_next(pos[ch], prev)
            if nxt is None:
                found = False
                break
            prev = nxt
        if found:
            res += 1
    return res


print(Solve("abcde", ["a", "bb", "acd", "ace"]))  # 3
print(Solve("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))  # 2

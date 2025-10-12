class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapping = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in mapping:
                if not stk or stk[-1] != mapping[ch]:
                    return False
                stk.pop()
            else:
                stk.append(ch)

        return not stk

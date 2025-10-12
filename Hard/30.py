from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        lenword = len(words[0])
        lenwords = lenword * len(words)
        word_count = Counter(words)
        res = []

        for offset in range(lenword):
            left = offset
            seen = Counter()
            count = 0

            for right in range(offset, len(s) - lenword + 1, lenword):
                word = s[right : right + lenword]

                # If it's a valid word, add to window
                if word in word_count:
                    seen[word] += 1
                    count += 1

                    # If too many of this word → shrink from left
                    while seen[word] > word_count[word]:
                        left_word = s[left : left + lenword]
                        seen[left_word] -= 1
                        left += lenword
                        count -= 1

                    # If window matches exactly all words
                    if count == len(words):
                        res.append(left)

                else:
                    # reset window
                    seen.clear()
                    count = 0
                    left = right + lenword

        return res

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for ast in asteroids:
            skip = False
            if ast < 0:
                while s and s[-1] > 0:
                    if s[-1] < -ast :
                        s.pop()
                    elif s[-1] == -ast:
                        s.pop()
                        skip = True
                        break
                    else:
                        skip = True
                        break

            if not skip:
                s.append(ast)

        return s

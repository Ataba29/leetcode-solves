from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(x, y):
            res = []
            i,j = 0,0

            while i < len(x) and j < len(y):
                if x[i] > y[j]:
                    res.append(y[j])
                    j+=1
                else:
                    res.append(x[i])
                    i+=1
                
            res.extend(x[i:])
            res.extend(y[j:])

            return res
        
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            m = len(arr) // 2

            left = mergeSort(arr[:m])
            right = mergeSort(arr[m:])

            return merge(left, right)

        return mergeSort(nums)
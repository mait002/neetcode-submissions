# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)
        s = 0
        e = n - 1
        return self.helper_mergeSort(pairs, s, e)

    def helper_mergeSort(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs
        else:
            mid = (e+s)//2
            self.helper_mergeSort(pairs, s, mid)
            self.helper_mergeSort(pairs, mid+1, e)
            return self.merge(pairs, s, mid, e) 
       

    def merge(self, pairs: List[Pair], s, m, e) -> List[Pair]:
        l = 0
        r = 0
        k = s

        left = pairs[s:m+1]
        right = pairs[m+1:e+1]

        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                pairs[k] = left[l]
                l+=1
                k+=1
            else:
                pairs[k] = right[r]
                r+=1
                k+=1

        while l < len(left):
            pairs[k] = left[l]
            l+=1
            k+=1
        while r < len(right):
            pairs[k] = right[r]
            r+=1
            k+=1
        return pairs


        

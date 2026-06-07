# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
import copy
class Solution:
    
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        progress = []
       
        #'''
        if pairs == []:
            return []
        for i in range(1, len(pairs)):
            progress.append(copy.deepcopy(pairs))
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j+1].key:
                temp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                
                j -= 1
        #'''
        progress.append(copy.deepcopy(pairs))
        return progress
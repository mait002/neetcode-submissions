class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = []
        i = 0
        while len(lst) != len(nums):
            if nums[i] not in lst:
                lst.append(nums[i])
            else:
                return True
            i+=1
        return False

        
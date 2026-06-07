class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = []
        for i in nums:
            if i not in n:
                n.append(i)
        
        nums.clear()

        for i in n:
            nums.append(i)

        return len(nums)


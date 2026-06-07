class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        lst = []
        for i in range(len(nums)):
            if nums[i] == val:
                for j in range(i, len(nums)):
                    if nums[j] != val:
                        nums[i] = nums[j]
                        nums[j] = val
                        break
        
    
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
                k+=1
        

        return len(nums)-k
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        rem = {}

        for i in range(len(nums)):

            left = target - nums[i]

            if left in rem:
                return [rem[left], i]
            
            rem[nums[i]] = i
        
        return []





        
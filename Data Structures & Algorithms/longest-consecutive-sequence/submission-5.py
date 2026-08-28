class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if (n <= 1):
            return n
        

        max_len = 1
        i = 0
        j = 1
        nums.sort()
        print(nums)
        next_num = nums[i]+1

        while j < n:
            if (nums[j] == next_num):
                
                max_len = max(max_len, j-i+1)
                next_num = nums[j]+1
            elif (nums[j] == nums[j-1]):
                i+=1
                
                
            else:
                max_len = max(max_len, j-i-1)
                i = j
                next_num = nums[i]+1
                

            j+=1
            

        return max_len

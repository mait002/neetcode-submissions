class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        n = len(num_set)

        if (n <= 1):
            return n

        max_len = 0

        for num in num_set:
            if (num-1) not in num_set:
                
                curr = num
                count = 1
                
                while (curr+1) in num_set:
                    curr += 1
                    count += 1
                max_len = max(max_len, count)
                
            

        return max_len



public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int n = nums.Length;
        int[] prefix = new int[n];
        int[] postfix = new int[n];
        int[] output = new int[n];
        prefix[0] = nums[0];
        Console.WriteLine($"Prefix value at position 0 is {nums[0]}");
        postfix[n-1] = nums[n-1];
        Console.WriteLine($"Postfix value at position {n-1} is {nums[n-1]}");
        

        for (int i = 1; i < n; i++)
        {
            prefix[i] = prefix[i-1]*nums[i];
            Console.WriteLine($"Prefix value at position {i} is {prefix[i]}");
            postfix[n-i-1] = postfix[n-i]*nums[n-i-1];
            Console.WriteLine($"Postfix value at position {n-i-1} is {postfix[n-i-1]}");

        }
        
        
        for (int j = 0; j < n; j++)
        {
            if (j == 0)
            {
                output[j] = postfix[j+1];
            }
            else if (j == n-1){
                output[j] = prefix[j-1];
            }
            else
            {
                output[j] = prefix[j-1]*postfix[j+1];
            }
            
        }

        return output;
        
    }
}

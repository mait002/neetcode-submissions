public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> count = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++){
            if (count.ContainsKey(nums[i])){
                count[nums[i]]++;
            }
            else{
                count[nums[i]] = 1;
            }
        }
        int[] res = count.OrderByDescending(kvp => kvp.Value).Select(kvp => kvp.Key).Take(k).ToArray();
        
        return res;
        
    }
}

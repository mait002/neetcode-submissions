public class Solution {
    public int[] TwoSum(int[] nums, int target) {

        int[] res = {-1,-1};
        Dictionary<int, int> dict = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++){
            int rest = target - nums[i];

            if (dict.ContainsKey(rest)){
                res[0] = dict[rest];
                res[1] = i;
                return res;
            }
            else{
                dict[nums[i]] = i;
            }

        }
        return res;


    }
}

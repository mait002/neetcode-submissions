class Solution {
    public int[] getConcatenation(int[] nums) {

        int[] ans = new int[2*nums.length];
        int i = 0;
        while (i < nums.length*2){
            if (i > nums.length-1){
                ans[i] = nums[i - nums.length];
            }
            else{
                ans[i] = nums[i];
            }
            i++;

        }
        return ans;
        
    }
}
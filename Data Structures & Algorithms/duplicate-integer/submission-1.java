class Solution {
    public boolean hasDuplicate(int[] nums) {
        ArrayList<Integer> lst = new ArrayList<Integer>();
        for(int i = 0; i < nums.length; i++){
            if (lst.contains(nums[i])){
                return true;
            }else{
                lst.add(nums[i]);

            }
        }
        return false;
        
    }
}
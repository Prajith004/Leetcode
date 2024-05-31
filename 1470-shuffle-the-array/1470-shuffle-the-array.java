class Solution {
    public int[] shuffle(int[] nums, int n) {
        int ans[]=new int[2*n];
        int temp=n;
        int j=0;
        for(int i=0;i<n;i++){
            ans[j++]=nums[i];
            ans[j++]=nums[temp];
            temp=temp+1;
            }
        return ans;
    }
}
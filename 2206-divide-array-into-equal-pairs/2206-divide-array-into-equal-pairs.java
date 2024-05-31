class Solution {
    public boolean divideArray(int[] nums) {
        int pairs=0;
        int n=nums.length;
        boolean a=false;
        for(int i=0;i<n-1;i++){
            int count=0;
            
            for(int j=i+1;j<n;j++){
                if(nums[i]==nums[j] && nums[i]!=0){
                    count=count+1;
                    pairs=pairs+1;
                    nums[i]=0;
                    nums[j]=0;
                
                    
                    //continue;
                    break;
                    
                    }
                }
                
            }
        if(pairs==n/2){
            a=true;
        }
        return a;
    }
    
}


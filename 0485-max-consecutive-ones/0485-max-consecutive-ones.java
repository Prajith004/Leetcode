class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
         int n = nums.length;
    int[] result = new int[n]; // Corrected the declaration of the result array
    int maxCount = 0; // Variable to store the maximum consecutive ones count

    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = i; j < n; j++) {
            if (nums[j] == 1) {
                count++;
            } else {
                break; // Break the inner loop if the current element is not 1
            }
        }
        result[i] = count; // Store the consecutive ones count for the current position
        if (count > maxCount) {
            maxCount = count; // Update the maximum consecutive ones count if needed
        }
    }

    return maxCount; // Return the maximum consecutive ones count 
    }
    
}
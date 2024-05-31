class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        
        int n1 = nums1.length;
        int n2 = nums2.length;
        int[] result = new int[n1];
        for (int i = 0; i < n1; i++) {
            boolean found = false;
            for (int j = 0; j < n2; j++) {
                if (nums1[i] == nums2[j]) {
                    found = true;
                    int nextGreater = -1; // Initialize to -1, assuming no next greater element found
                    for (int k = j + 1; k < n2; k++) {
                        if (nums2[k] > nums1[i]) {
                            nextGreater = nums2[k];
                            break;
                        }
                    }
                    result[i] = nextGreater; // Store the next greater element's value
                    break;
                }
            }
            if (!found) {
                result[i] = -1;
            }
        }
        return result;
    }
}

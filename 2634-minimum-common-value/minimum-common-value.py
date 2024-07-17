class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums2_set = set(nums2)
        
        
        for ele in nums1:
            if ele in nums2_set:
                return ele
        
        
        return -1

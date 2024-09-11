class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        for ele in nums1:
            if ele in nums2:
                lst.append(ele)
        return list(set(lst))
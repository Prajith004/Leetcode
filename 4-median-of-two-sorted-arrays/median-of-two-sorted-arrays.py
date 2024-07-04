class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1=[]
        for ele in nums1:
            l1.append(ele)
        for ele in nums2:
            l1.append(ele)
        l1.sort()
        n=len(l1)
        if n%2!=0:
            mid=n//2
            return l1[mid]
        else:
            mid1=n//2
            mid2=mid1-1
            num=(l1[mid1]+l1[mid2])/2
            return num

        
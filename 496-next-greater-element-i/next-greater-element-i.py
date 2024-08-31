class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        
        for ele in nums1:
            
            idx=nums2.index(ele)
            for i in range(idx+1,len(nums2)):
                if nums2[i]>ele:
                    lst.append(nums2[i])
                    break
            else:
                lst.append(-1)
                    
            
        return lst



        
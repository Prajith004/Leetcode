class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        indx=nums.index(target)
        if nums.count(target)==1:
            return [indx,indx]
        el_c=1
        count=nums.count(target)
        for i in range(indx+1,len(nums)):
            if nums[i]==target:
                el_c+=1
                if el_c==count:
                    return [indx,i]
        
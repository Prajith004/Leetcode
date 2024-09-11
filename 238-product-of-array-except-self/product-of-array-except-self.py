class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n =len(nums)
        l=1
        r=1
        result=[0]*n
        for i in range(n):
            result[i]=l
            l*=nums[i]
        for i in range(n-1,-1,-1):
            result[i]*=r
            r*=nums[i]
        return result

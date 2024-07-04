class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        l1=[]
        for i in range(0,n+1):
            l1.append(i)
        for ele in l1:
            if ele not in nums:
                return ele

        
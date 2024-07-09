class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=0
        for ele in nums:
            count=nums.count(ele)
            if count==1:
                return ele
                break
        
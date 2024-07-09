class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count=0
        lst=[]
        for ele in nums:
            count=nums.count(ele)
            if count==1:
                lst.append(ele)
        return lst


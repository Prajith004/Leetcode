class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lst=[]
        for ele in nums:
            lst.append(ele)
        for ele in lst:
            if ele==val:
                nums.remove(ele)
                
        return len(nums)
        
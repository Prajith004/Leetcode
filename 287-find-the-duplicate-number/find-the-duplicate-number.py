class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s_n=set()
        for i in nums:
            if i in s_n:
                return i
            s_n.add(i)



        
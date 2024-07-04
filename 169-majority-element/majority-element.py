import statistics as s
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=s.mode(nums)
        return n
        
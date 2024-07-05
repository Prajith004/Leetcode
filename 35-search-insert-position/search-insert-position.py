class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for i, ele in enumerate(nums):
            if ele > target:
                return i
        
        # If the target is greater than all elements in nums, return the length of nums
        return len(nums)
        
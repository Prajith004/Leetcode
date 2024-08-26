class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        lst=[]
        for idx,n in enumerate(nums):
            if n==target:
                lst.append(idx)
        return lst

            
        
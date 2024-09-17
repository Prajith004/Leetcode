class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        front=0
        
        lst=[]
        while front<len(nums):
            next=front+1
            while next<len(nums):
                if nums[front]+nums[next]==target:
                    return [front,next]
                else:
                    next+=1
            front+=1
        return []


        
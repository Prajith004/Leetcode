class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
        if len(nums)==1 and nums[0]==target:
            return 0
 
        while low <= high:
    
            mid = (high + low) // 2
    
            
            if nums[mid] < target:
                low = mid + 1
    
            
            elif nums[mid] > target:
                high = mid - 1
    
           
            else:
                return mid
    
       
        return -1
    



            
        
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        lst=[]
        for i in range(len(nums)//2):
            MIN=min(nums)
            MAX=max(nums)
            nums.remove(MIN)
            nums.remove(MAX)
            avg=(MIN+MAX)/2
            lst.append(avg)
        return min(lst)

       
        
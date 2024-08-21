class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for lst1 in grid:
            for ele in lst1:
                if ele<0:
                    count+=1
        return count
        
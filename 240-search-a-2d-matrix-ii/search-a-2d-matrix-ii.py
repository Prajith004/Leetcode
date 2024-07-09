class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for n_l in matrix:
            for ele in n_l:
                if ele==target:
                    return True
                    break
        else:
            return False
        
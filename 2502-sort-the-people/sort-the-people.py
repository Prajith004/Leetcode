class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        r_d = list(zip(names, heights))
        r_l = []
        sorted_keys = sorted(r_d, key=lambda x: x[1], reverse=True)
        for i in range(len(sorted_keys)):

            r_l.append(sorted_keys[i][0])

        return r_l

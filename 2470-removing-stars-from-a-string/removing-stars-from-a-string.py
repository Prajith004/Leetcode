class Solution:
    def removeStars(self, s: str) -> str:
        lst=[]
        for ch in s:
            if ch=="*":
                if len(lst)>0:
                    lst.pop()
            else:
                lst.append(ch)
        return "".join(lst)
        
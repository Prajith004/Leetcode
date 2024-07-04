class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str=''
        for num in digits:
            num_str=num_str+str(num)
        num=int(num_str)+1
        num_str=str(num)
        digits=[]
        for i in range(len(num_str)):
            ele=int(num_str[i])
            digits.append(ele)
        return digits




        
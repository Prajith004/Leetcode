class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        for i in range(len(flowerbed)):
            if i>0  and i<len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
                count+=1
                flowerbed[i]=1
            elif i == 0 and flowerbed[i] == 0 and (len(flowerbed)== 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
            elif i==len(flowerbed)-1 and flowerbed[i-1]==0 and flowerbed[i]==0 :
                count+=1
                flowerbed[i]=1
        return count>=n


        
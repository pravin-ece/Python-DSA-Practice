class Solution:
    def getSecondLargest(self, arr):
        lar=arr[0]
        slar=-1
        a=len(arr)
        for i in range(1,a):
            if arr[i]>lar:
                slar=lar
                lar=arr[i]
                
            elif arr[i]>slar and arr[i]<lar:
                slar=arr[i]
        return slar
        

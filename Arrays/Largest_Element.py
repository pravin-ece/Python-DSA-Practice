class Solution:
    def largest(self, arr):
        a=len(arr)
        largest=arr[0]
        for i in range(1,a):
            if arr[i]>largest:
                largest=arr[i]
        return largest
                

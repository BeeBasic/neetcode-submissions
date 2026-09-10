class Solution:
    def findMin(self, arr: List[int]) -> int:
        defaultt = arr[0]
        for i in range(len(arr)-1):
            if(arr[i+1]<arr[i]):
                defaultt = arr[i+1]
        return defaultt
                
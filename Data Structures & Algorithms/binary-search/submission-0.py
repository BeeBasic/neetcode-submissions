class Solution:
    def search(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr)-1
        while(left<=right):
            mid = (left+right)//2
            if(arr[mid]==k):
                return mid
            
            if(arr[mid]<k):
                left=mid+1
            else:
                right=mid-1
        return -1
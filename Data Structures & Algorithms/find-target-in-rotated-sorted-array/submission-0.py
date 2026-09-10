class Solution:
    def search(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == k:
                return mid

            # Left half is sorted
            if arr[left] <= arr[mid]:
                if arr[left] <= k < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:
                if arr[mid] < k <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
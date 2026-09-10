import math

class Solution:

    def hours_needed(self, piles, k):
        hours = 0

        for i in piles:
            hours += math.ceil(i / k)

        return hours

    def minEatingSpeed(self, piles, h):
        mi = 1
        mx = max(piles)

        while mi <= mx:
            mid = (mi + mx) // 2

            if self.hours_needed(piles, mid) <= h:
                mx = mid - 1
            else:
                mi = mid + 1

        return mi
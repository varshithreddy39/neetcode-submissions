class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            hours=0
            for num in piles:
                hours+=(num+mid-1)//mid
            if hours<=h:
                high=mid-1
            else:
                low=mid+1
        return low
            

        
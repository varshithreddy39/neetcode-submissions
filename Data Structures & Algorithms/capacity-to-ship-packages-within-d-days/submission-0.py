class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)

        while low<=high:
            mid=(low+high)//2
            load=0
            day=1

            for i in weights:
                if i+load>mid:
                    day+=1
                    load=i
                else:
                    load+=i
            if day<=days:
                high=mid-1
            else:
                low=mid+1
        return low

        
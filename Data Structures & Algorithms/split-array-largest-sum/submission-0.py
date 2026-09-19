class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)

        while low<=high:
            mid=(low+high)//2
            total=0 
            splits=1

            for i in range(len(nums)):
                if nums[i]+total>mid:
                    splits+=1
                    total=nums[i]
                else:
                    total+=nums[i]
            if splits<=k:
                high=mid-1
            else:
                low=mid+1
        return low

        
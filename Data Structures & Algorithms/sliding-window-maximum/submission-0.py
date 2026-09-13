class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        window=[]
        ans=[]
        for r in range(len(nums)):
            if r-l+1<=k:
                window.append(nums[r])
            if r-l+1==k:
                ans.append(max(window))
                del window[0]
                l+=1
        return ans

        
        
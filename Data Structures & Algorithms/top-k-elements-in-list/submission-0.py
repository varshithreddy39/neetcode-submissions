class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        ans=[]
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1

        for num in freq:
            if freq[num]>=k:
                ans.append(num)
        return ans
        
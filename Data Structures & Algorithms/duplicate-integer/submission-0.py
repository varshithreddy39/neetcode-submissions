class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqs={}

        for i in range(len(nums)):
            freqs[nums[i]]=freqs.get(nums[i],0)+1
        for freq in freqs:
            if freqs[freq]>1:
                return True
        return False
        
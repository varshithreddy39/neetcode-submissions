class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}

        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        for v in freq.values():
            if v>1:
                return True
        return False
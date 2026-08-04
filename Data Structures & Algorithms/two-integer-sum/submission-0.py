class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            need=target-nums[i]
            if need in freq:
                return [freq[need],i]
            freq[nums[i]]=i
        
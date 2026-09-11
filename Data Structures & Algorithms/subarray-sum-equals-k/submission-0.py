class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        freq={0:1}
        prefix_sum=0

        for i in range(len(nums)):
            prefix_sum+=nums[i]
            need=prefix_sum-k
            if need in freq:
                count+=freq[need]
            freq[prefix_sum]=freq.get(prefix_sum,0)+1
        return count
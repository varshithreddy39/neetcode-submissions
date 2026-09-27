class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1

        for f in freq:
            if freq[f]>1:
                return f
        
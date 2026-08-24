class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_lenght=0
        s=set(nums)

        for num in nums:
            if num-1 not in s:
                current=num
                lenght=1
            while current+1 in s:
                current+=1
                lenght+=1
            max_lenght=max(max_lenght,lenght)
        return max_lenght
        
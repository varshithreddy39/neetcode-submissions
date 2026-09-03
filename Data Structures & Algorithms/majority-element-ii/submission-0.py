class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        n=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1

        for i in freq:
            if freq[i]>len(nums)//3:
                n.append(i)
        return n
        
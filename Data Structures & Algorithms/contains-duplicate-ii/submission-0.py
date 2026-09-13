class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        j=len(nums)-1

        while i <j:
            if nums[i]==nums[j]and abs(i-j)<=k:
                return True
                break
            i+=1
            j-=1
        return False
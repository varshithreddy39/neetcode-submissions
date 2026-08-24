class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1

        for i in range(len(numbers)):
            sum=numbers[left]+numbers[right]
            if sum==target:
                return [numbers[left],numbers[right]]
            elif sum>target:
                right-=1
            else:
                left+=1

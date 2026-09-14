class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums,low,mid,high):
            left=nums[low:mid+1]
            right=nums[mid+1:high+1]
            i=0
            j=0
            k=low

            while i <len(left) and j<len(right):
                if left[i]<right[j]:
                    nums[k]=left[i]
                    i+=1
                else:
                    nums[k]=right[j]
                    j+=1
                k+=1
            while i<len(left):
                nums[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                nums[k]=right[j]
                j+=1
                k+=1
        
        
        def merge_sort(nums, low, high):

            if low >= high:
                return

            mid = (low + high) // 2

            merge_sort(nums, low, mid)
            merge_sort(nums, mid + 1, high)

            merge(nums, low, mid, high)

        merge_sort(nums, 0, len(nums) - 1)

        return nums


        
        
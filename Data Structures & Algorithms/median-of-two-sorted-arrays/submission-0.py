class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            return self.findMedianSortedArrays(nums2,nums1)
        n1=len(nums1)
        n2=len(nums2)
        low=0
        high=n1

        while low<=high:
            cut1=(low+high)//2
            cut2=(n1+n2+1)//2-cut1

            if cut1==0:
                left1=float("-inf")
            else:
                left1=nums1[cut1-1]
            if cut2==0:
                left2=float("-inf")
            else:
                left2=nums2[cut2-1]
            if cut1==n1:
                right1=float("inf")
            else:
                right1=nums1[cut1]
            if cut2==n2:
                right2=float("inf")
            else:
                right2=nums2[cut2]
            if left1<=right2 and left2<=right1:
                if (n1+n2)%2==0:
                    return (max(left1,left2)+min(right1,right2))/2
                else:
                    return (max(left1,left2))
            elif left1 >right2:
                high=cut1-1
            else:
                low=cut1+1
        
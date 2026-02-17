class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        allnum = sorted(nums1 + nums2)
        n = len(allnum)
        mid = n // 2
        
        if n % 2 == 0:
           
            return (allnum[mid - 1] + allnum[mid]) / 2.0
        else:
           
            return float(allnum[mid])
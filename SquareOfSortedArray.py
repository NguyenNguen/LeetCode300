class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums1 = []
        for i in range(0,len(nums)):
            nums1.append(nums[i]**2)
        nums1.sort()
        return(nums1)
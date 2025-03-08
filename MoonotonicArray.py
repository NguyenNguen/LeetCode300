class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums0 =[]
        for n in nums:
            nums0.append(n)
        nums.sort()
        nums1 = nums[::-1]
        if nums == nums0 or nums0 == nums1:
            return(True)
        else:
            return(False)
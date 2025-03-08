class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return(0)
        num3 = nums
        nums2 = list(dict.fromkeys(nums))
        for numbers in nums2:
            if numbers in nums:
                nums.remove(numbers)
        for n in num3:
            if n in nums2:
                nums2.remove(n)
        return(nums2[0])     
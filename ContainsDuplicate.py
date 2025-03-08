class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums2 = list(dict.fromkeys(nums))
        if len(nums)==len(nums2):
            return (False)
        else:
            return (True)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (0,len(nums)-1,1):
            for j in range (1,len(nums),1):
                if i!=j and nums[i] + nums[j] == target:
                    return [i,j]
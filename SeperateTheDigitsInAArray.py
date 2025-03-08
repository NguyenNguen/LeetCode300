class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [str(n) for n in nums]
        list1 = []
        list2 = []
        for n in nums:
            list1.append(list(n))
        for items in list1:
            for number in items:
                list2.append(number)
        return((list(map(int,list2))))
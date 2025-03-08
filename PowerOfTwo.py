class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = n
        if i == 1:
            return (True)
        elif i%2 != 0 or i <= 0 and i!= 1:
            return (False)
        else:
            while i % 2 == 0:
                i=i/2
        if i == 1:
            return (True)
        else:
            return (False)
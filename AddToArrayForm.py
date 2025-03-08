class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        s = 0
        for i in range(0,len(num)):
            s += num[i]*10**(len(num)-1-i)
        s = s + k
        list1 = list((int(t) for t in list(str(s))))
        return(list1)
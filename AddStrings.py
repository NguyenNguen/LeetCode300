class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = 0
        num1 = [int(n) for n in num1][::-1]
        num2 = [int(n) for n in num2][::-1]
        for i in range(0,len(num1)):
            a += num1[i]*(10**i)
        for t in range(0,len(num2)):
            a += num2[t]*(10**t)
        return(str(a))
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        list1 = list(s[len(s)-1])
        return(len(list1))
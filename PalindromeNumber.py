class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        x2 = x[::-1]
        if x == x2 :
            return(True)
        else: 
            return(False)
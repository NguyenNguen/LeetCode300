class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = 1
        digits = digits[::-1]
        for i in range (0,len(digits)):
            k += digits[i]*(10**i)
        list1 = list(int(n) for n in str(k))
        return(list1)
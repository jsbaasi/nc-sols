class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n-1
        carry = 1
        while i>=0:
            sum = digits[i]+carry
            carry = sum//10
            digits[i] = sum%10
            i-=1
        return [carry]+digits if carry else digits
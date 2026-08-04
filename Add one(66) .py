class Solution(object):
    def plusOne(self, digits):
        num = 0
        for i in digits:
            num = num*10 + i
        num += 1
        new_digits = []
        while num > 0:
            rem = num % 10
            new_digits.insert(0, rem)
            num //= 10
        return new_digits
        

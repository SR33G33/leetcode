# 7. Reverse Integer

# Given a signed 32-bit integer x , return x with its digits reversed .
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31 , (2^31) - 1] , then return 0 .
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1: Input: x = 123 Output: 321
# Example 2: Input: x = -123 Output: -321
# Example 3: Input: x = 120 Output: 21 
# Constraints: -2 31 <= x <= 2 31 - 1

class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        strInt = str(x)
        reversed = 0
        if strInt[0] == '-':
            neg = -1
            strInt = strInt[1:]

        for i in range (len(strInt)):
            print(reversed)
            idx = len(strInt) - 1 - i
            if(neg == -1 and ((2**31)-int(strInt[idx]))/10 >= reversed):
                reversed = reversed * 10 + int(strInt[idx])
            elif(((2**31)-1-int(idx))/10 >= reversed):
                reversed = reversed * 10 + int(strInt[idx])
            else:
                return 0

        return neg*reversed

s = Solution()
# print(s.reverse(123))
# print(s.reverse(-123))
# print(s.reverse(120))
print(s.reverse(1534236469))


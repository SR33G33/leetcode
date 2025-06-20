# 537. Complex Number Multiplication

# A complex number can be represented as a string on the form " real + imaginary i" where: real is the real part and is an integer in the range [-100, 100] . imaginary is the imaginary part and is an integer in the range [-100, 100] . i 2 == -1 .
# Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications .
# Example 1: Input: num1 = "1+1i", num2 = "1+1i" Output: "0+2i" Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
# Example 2: Input: num1 = "1+-1i", num2 = "1+-1i" Output: "0+-2i" Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
# Constraints: num1 and num2 are valid complex numbers.

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        return

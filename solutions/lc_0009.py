# 9. Palindrome

# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        for i in range(len(s)/2 + 1):
            if(s[i] != s[len(s)-1-i]): return False
        return True
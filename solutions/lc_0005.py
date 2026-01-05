# 5. Longest Palindromic Substring

# Given a string s , return the longest palindromic substring in s .
# Example 1: Input: s = "babad" Output: "bab" Explanation: "aba" is also a valid answer.
# Example 2: Input: s = "cbbd" Output: "bb" Constraints: 1 <= s.length <= 1000 s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestLen = 1
        longestPal = s[0]
        for center in range(len(s)):
            # Odd Palindromes (single center)
            left, right = center, center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currentLen = right - left + 1
                if currentLen > longestLen:
                    longestLen = currentLen
                    longestPal = s[left:right+1]
                left -= 1
                right += 1


            # Even Palindromes (two letter center)
            left, right = center, center + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currentLen = right - left + 1
                if currentLen > longestLen:
                    longestLen = currentLen
                    longestPal = s[left:right+1]
                left -= 1
                right += 1
        return longestPal
    
s = Solution()
print(s.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(s.longestPalindrome("cbbd"))   # Output: "bb"
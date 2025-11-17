# 5. Longest Palindromic Substring

# Given a string s , return the longest palindromic substring in s .
# Example 1: Input: s = "babad" Output: "bab" Explanation: "aba" is also a valid answer.
# Example 2: Input: s = "cbbd" Output: "bb" Constraints: 1 <= s.length <= 1000 s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        left_i = 0
        right_i = 0
        seen = {}
        max_len = 0

        if(len(s) == 0 or len(s) == 1):
            return len(s)

        while right_i < len(s):
            if(s[right_i] not in seen):
                seen[s[right_i]] = False
            
            while(seen[s[right_i]] == True):
                # print(s)
                # print(f"{left_i}, {right_i} ")
                seen[s[left_i]] = False
                left_i += 1
         
            seen[s[right_i]] = True
            max_len = max(max_len, right_i - left_i + 1)

            right_i += 1

        return max_len  

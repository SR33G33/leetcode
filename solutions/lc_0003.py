# 3. Longest Substring Without Repeating Characters

# Given a string s , find the length of the longest substring without duplicate characters.
# Example 1: Input: s = "abcabcbb" Output: 3 Explanation: The answer is "abc", with the length of 3.
# Example 2: Input: s = "bbbbb" Output: 1 Explanation: The answer is "b", with the length of 1.
# Example 3: Input: s = "pwwkew" Output: 3 Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Constraints: 0 <= s.length <= 5 * 10 4 s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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

sol = Solution()

print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
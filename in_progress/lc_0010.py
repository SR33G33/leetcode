# 10. Regular Expression Matching

# Given an input string s and a pattern p , implement regular expression matching with support for '.' and '*' where: '.' Matches any single character.​​​​ '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# Example 1: Input: s = "aa", p = "a" Output: false Explanation: "a" does not match the entire string "aa".
# Example 2: Input: s = "aa", p = "a*" Output: true Explanation: '*' means zero or more of the preceding element, 'a'.
# Therefore, by repeating 'a' once, it becomes "aa".
# Example 3: Input: s = "ab", p = ".*" Output: true Explanation: ".*" means "zero or more (*) of any character (.)".
# Constraints: 1 <= s.length <= 20 1 <= p.length <= 20 s contains only lowercase English letters. p contains only lowercase English letters, '.' , and '*' .
# It is guaranteed for each appearance of the character '*' , there will be a previous valid character to match.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_i = 0
        star = False

        if(p == s): return True

        while len(s) > 0 and p_i < len(p):
            curr_match = p[p_i]
            if(p_i < len(p)-1): 
                if(p[p_i + 1] == '*'):
                    star = True
                    p_i += 1
            if(star):
                while (s[0] == curr_match or curr_match == '.'):
                    if(len(s) == 1): return p_i == len(p)-1
                    s = s[1:]
            else:
                # print(f"{s}, curr match = {curr_match}")
                # print(f"first elem and curr {s[0] == curr_match or curr_match =='.'}")
                if(s[0] == curr_match or curr_match == '.'): s = s[1:]
                else: return False
            p_i += 1
            star = False
        print(p_i)
        print(s)
        return (len(s) == 0 and p_i == len(p))

s = Solution()
print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "aa"))
print(s.isMatch("aab", "aa"))
print(s.isMatch("aab", ".*"))
print(s.isMatch("ab", ".*c"))
# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        strs.sort(key=len, reverse=True)
        longest_str = strs[0]
        longest_len = len(longest_str)
        prefix = ""

        for i in range (longest_len):
            if(self.checkCharsAtIndex(strs, i)):
                prefix += longest_str[i]
            else: break
        return prefix

    
    def checkCharsAtIndex(self, strs, i):
        current_char = strs[0][i]
        for str in strs:
            if(i >= len(str)): return False
            if(str[i] != current_char): return False
        
        return True
    

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
print(sol.longestCommonPrefix(["cir","car"]))

# 58. Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        on_word = False
        word_len = 0

        for i in range(len(s)-1, -1, -1):
            # print(s[i])
            if(s[i] != " "):
                if not on_word:
                    on_word = True
                    word_len += 1
                else: word_len += 1
            else:
                if on_word: 
                    return word_len
        return word_len
                    
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("   fly me   to   the moon  "))
print(sol.lengthOfLastWord("luffy is still joyboy"))


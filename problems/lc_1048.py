# 1048. Longest String Chain

# You are given an array of words where each word consists of lowercase English letters. word A is a predecessor of word B if and only if we can insert exactly one letter anywhere in word A without changing the order of the other characters to make it equal to word B .
# For example, "abc" is a predecessor of "ab a c" , while "cba" is not a predecessor of "bcad" .
# A word chain is a sequence of words [word 1 , word 2 , ..., word k ] with k >= 1 , where word 1 is a predecessor of word 2 , word 2 is a predecessor of word 3 , and so on.
# A single word is trivially a word chain with k == 1 .
# Return the length of the longest possible word chain with words chosen from the given list of words .
# Example 1: Input: words = ["a","b","ba","bca","bda","bdca"] Output: 4 Explanation : One of the longest word chains is ["a"," b a","b d a","bd c a"].
# Example 2: Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"] Output: 5 Explanation: All the words can be put in a word chain ["xb", "xb c ", " c xbc", " p cxbc", "pcxbc f "].
# Example 3: Input: words = ["abcd","dbqca"] Output: 1 Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
# ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
# Constraints: 1 <= words.length <= 1000 1 <= words[i].length <= 16 words[i] only consists of lowercase English letters.

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        return

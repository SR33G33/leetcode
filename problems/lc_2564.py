# 2564. Substring XOR Queries

# You are given a binary string s , and a 2D integer array queries where queries[i] = [first i , second i ] .
# For the i th query, find the shortest substring of s whose decimal value , val , yields second i when bitwise XORed with first i .
# In other words, val ^ first i == second i .
# The answer to the i th query is the endpoints ( 0-indexed ) of the substring [left i , right i ] or [-1, -1] if no such substring exists.
# If there are multiple answers, choose the one with the minimum left i .
# Return an array ans where ans[i] = [left i , right i ] is the answer to the i th query.
# A substring is a contiguous non-empty sequence of characters within a string.
# Example 1: Input: s = "101101", queries = [[0,5],[1,2]] Output: [[0,2],[2,3]] Explanation: For the first query the substring in range [0,2] is "101" which has a decimal value of 5 , and 5 ^ 0 = 5 , hence the answer to the first query is [0,2] .
# In the second query, the substring in range [2,3] is "11", and has a decimal value of 3 , and 3 ^ 1 = 2 .
# So, [2,3] is returned for the second query.
# Example 2: Input: s = "0101", queries = [[12,8]] Output: [[-1,-1]] Explanation: In this example there is no substring that answers the query, hence [-1,-1] is returned .
# Example 3: Input: s = "1", queries = [[4,5]] Output: [[0,0]] Explanation: For this example, the substring in range [0,0] has a decimal value of 1 , and 1 ^ 4 = 5 .
# So, the answer is [0,0] .
# Constraints: 1 <= s.length <= 10 4 s[i] is either '0' or '1' . 1 <= queries.length <= 10 5 0 <= first i , second i <= 10 9

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        return

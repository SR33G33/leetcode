# 3145. Find Products of Elements of Big Array

# The powerful array of a non-negative integer x is defined as the shortest sorted array of powers of two that sum up to x .
# The table below illustrates examples of how the powerful array is determined.
# It can be proven that the powerful array of x is unique. num Binary Representation powerful array 1 0000 1 [1] 8 0 1 000 [8] 10 0 1 0 1 0 [2, 8] 13 0 11 0 1 [1, 4, 8] 23 1 0 111 [1, 2, 4, 16] The array big_nums is created by concatenating the powerful arrays for every positive integer i in ascending order: 1, 2, 3, and so on.
# Thus, big_nums begins as [ 1 , 2 , 1, 2 , 4 , 1, 4 , 2, 4 , 1, 2, 4 , 8 , ...] .
# You are given a 2D integer matrix queries , where for queries[i] = [from i , to i , mod i ] you should calculate (big_nums[from i ] * big_nums[from i + 1] * ... * big_nums[to i ]) % mod i .
# Return an integer array answer such that answer[i] is the answer to the i th query.
# Example 1: Input: queries = [[1,3,7]] Output: [4] Explanation: There is one query. big_nums[1..3] = [2,1,2] .
# The product of them is 4.
# The result is 4 % 7 = 4.
# Example 2: Input: queries = [[2,5,3],[7,7,4]] Output: [2,2] Explanation: There are two queries.
# First query: big_nums[2..5] = [1,2,4,1] .
# The product of them is 8.
# The result is 8 % 3 = 2 .
# Second query: big_nums[7] = 2 .
# The result is 2 % 4 = 2 .
# Constraints: 1 <= queries.length <= 500 queries[i].length == 3 0 <= queries[i][0] <= queries[i][1] <= 10 15 1 <= queries[i][2] <= 10 5

class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        return

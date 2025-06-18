# 3288. Length of the Longest Increasing Path

# You are given a 2D array of integers coordinates of length n and an integer k , where 0 <= k < n . coordinates[i] = [x i , y i ] indicates the point (x i , y i ) in a 2D plane.
# An increasing path of length m is defined as a list of points (x 1 , y 1 ) , (x 2 , y 2 ) , (x 3 , y 3 ) , ..., (x m , y m ) such that: x i < x i + 1 and y i < y i + 1 for all i where 1 <= i < m . (x i , y i ) is in the given coordinates for all i where 1 <= i <= m .
# Return the maximum length of an increasing path that contains coordinates[k] .
# Example 1: Input: coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]], k = 1 Output: 3 Explanation: (0, 0) , (2, 2) , (5, 3) is the longest increasing path that contains (2, 2) .
# Example 2: Input: coordinates = [[2,1],[7,0],[5,6]], k = 2 Output: 2 Explanation: (2, 1) , (5, 6) is the longest increasing path that contains (5, 6) .
# Constraints: 1 <= n == coordinates.length <= 10 5 coordinates[i].length == 2 0 <= coordinates[i][0], coordinates[i][1] <= 10 9 All elements in coordinates are distinct . 0 <= k <= n - 1

class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        return

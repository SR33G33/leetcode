# 850. Rectangle Area II

# You are given a 2D array of axis-aligned rectangles .
# Each rectangle[i] = [x i1 , y i1 , x i2 , y i2 ] denotes the i th rectangle where (x i1 , y i1 ) are the coordinates of the bottom-left corner , and (x i2 , y i2 ) are the coordinates of the top-right corner .
# Calculate the total area covered by all rectangles in the plane.
# Any area covered by two or more rectangles should only be counted once .
# Return the total area .
# Since the answer may be too large, return it modulo 10 9 + 7 .
# Example 1: Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]] Output: 6 Explanation: A total area of 6 is covered by all three rectangles, as illustrated in the picture.
# From (1,1) to (2,2), the green and red rectangles overlap.
# From (1,0) to (2,3), all three rectangles overlap.
# Example 2: Input: rectangles = [[0,0,1000000000,1000000000]] Output: 49 Explanation: The answer is 10 18 modulo (10 9 + 7), which is 49.
# Constraints: 1 <= rectangles.length <= 200 rectanges[i].length == 4 0 <= x i1 , y i1 , x i2 , y i2 <= 10 9 x i1 <= x i2 y i1 <= y i2 All rectangles have non zero area.

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        return

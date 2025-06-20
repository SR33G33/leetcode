# 391. Perfect Rectangle

# Given an array rectangles where rectangles[i] = [x i , y i , a i , b i ] represents an axis-aligned rectangle.
# The bottom-left point of the rectangle is (x i , y i ) and the top-right point of it is (a i , b i ) .
# Return true if all the rectangles together form an exact cover of a rectangular region .
# Example 1: Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]] Output: true Explanation: All 5 rectangles together form an exact cover of a rectangular region.
# Example 2: Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]] Output: false Explanation: Because there is a gap between the two rectangular regions.
# Example 3: Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]] Output: false Explanation: Because two of the rectangles overlap with each other.
# Constraints: 1 <= rectangles.length <= 2 * 10 4 rectangles[i].length == 4 -10 5 <= x i < a i <= 10 5 -10 5 <= y i < b i <= 10 5

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        return

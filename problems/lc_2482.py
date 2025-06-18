# 2482. Difference Between Ones and Zeros in Row and Column

# You are given a 0-indexed m x n binary matrix grid .
# A 0-indexed m x n difference matrix diff is created with the following procedure: Let the number of ones in the i th row be onesRow i .
# Let the number of ones in the j th column be onesCol j .
# Let the number of zeros in the i th row be zerosRow i .
# Let the number of zeros in the j th column be zerosCol j . diff[i][j] = onesRow i + onesCol j - zerosRow i - zerosCol j Return the difference matrix diff .
# Example 1: Input: grid = [[0,1,1],[1,0,1],[0,0,1]] Output: [[0,0,4],[0,0,4],[-2,-2,2]] Explanation: - diff[0][0] = onesRow 0 + onesCol 0 - zerosRow 0 - zerosCol 0 = 2 + 1 - 1 - 2 = 0
# - diff[0][1] = onesRow 0 + onesCol 1 - zerosRow 0 - zerosCol 1 = 2 + 1 - 1 - 2 = 0
# - diff[0][2] = onesRow 0 + onesCol 2 - zerosRow 0 - zerosCol 2 = 2 + 3 - 1 - 0 = 4
# - diff[1][0] = onesRow 1 + onesCol 0 - zerosRow 1 - zerosCol 0 = 2 + 1 - 1 - 2 = 0
# - diff[1][1] = onesRow 1 + onesCol 1 - zerosRow 1 - zerosCol 1 = 2 + 1 - 1 - 2 = 0
# - diff[1][2] = onesRow 1 + onesCol 2 - zerosRow 1 - zerosCol 2 = 2 + 3 - 1 - 0 = 4
# - diff[2][0] = onesRow 2 + onesCol 0 - zerosRow 2 - zerosCol 0 = 1 + 1 - 2 - 2 = -2
# - diff[2][1] = onesRow 2 + onesCol 1 - zerosRow 2 - zerosCol 1 = 1 + 1 - 2 - 2 = -2
# - diff[2][2] = onesRow 2 + onesCol 2 - zerosRow 2 - zerosCol 2 = 1 + 3 - 2 - 0 = 2
# Example 2: Input: grid = [[1,1,1],[1,1,1]] Output: [[5,5,5],[5,5,5]] Explanation: - diff[0][0] = onesRow 0 + onesCol 0 - zerosRow 0 - zerosCol 0 = 3 + 2 - 0 - 0 = 5
# - diff[0][1] = onesRow 0 + onesCol 1 - zerosRow 0 - zerosCol 1 = 3 + 2 - 0 - 0 = 5
# - diff[0][2] = onesRow 0 + onesCol 2 - zerosRow 0 - zerosCol 2 = 3 + 2 - 0 - 0 = 5
# - diff[1][0] = onesRow 1 + onesCol 0 - zerosRow 1 - zerosCol 0 = 3 + 2 - 0 - 0 = 5
# - diff[1][1] = onesRow 1 + onesCol 1 - zerosRow 1 - zerosCol 1 = 3 + 2 - 0 - 0 = 5
# - diff[1][2] = onesRow 1 + onesCol 2 - zerosRow 1 - zerosCol 2 = 3 + 2 - 0 - 0 = 5 Constraints: m == grid.length n == grid[i].length 1 <= m, n <= 10 5 1 <= m * n <= 10 5 grid[i][j] is either 0 or 1 .

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        return

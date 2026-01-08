# 11. Container With Most Water

# You are given an integer array height of length n .
# There are n vertical lines drawn such that the two endpoints of the i th line are (i, 0) and (i, height[i]) .
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store .
# Notice that you may not slant the container.
# Example 1: Input: height = [1,8,6,2,5,4,8,3,7] Output: 49 Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.
# Example 2: Input: height = [1,1] Output: 1 Constraints: n == height.length 2 <= n <= 10 5 0 <= height[i] <= 10 4

class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        max_vol = 0
        while (left < right):
            volume = (right-left) * min(height[left], height[right])
            print(volume)
            if(volume > max_vol): max_vol = volume

            if(height[left] < height[right]): left += 1
            else: right -= 1

        return max_vol
    
s = Solution()

# print(s.maxArea([1,8,6,2,5,4,8,3,7]))
# print(s.maxArea([1,1]))
print(s.maxArea([8,7,2,1]))

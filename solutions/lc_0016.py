# 16. 3Sum Closest

# Given an integer array nums of length n and an integer target , find three integers in nums such that the sum is closest to target .
# Return the sum of the three integers .
# You may assume that each input would have exactly one solution.
# Example 1: Input: nums = [-1,2,1,-4], target = 1 Output: 2 Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2: Input: nums = [0,0,0], target = 1 Output: 0 Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
# Constraints: 3 <= nums.length <= 500 -1000 <= nums[i] <= 1000 -10 4 <= target <= 10 4

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def sumHelper(x,y, nums):
            return nums[x] + nums[y]

        nums.sort()
        closest = sum(nums[:3])


        for i in range(0, len(nums)):
            tmpNums = nums[0:i] + nums[i+1:]
            l = 0
            r = len(tmpNums)-1

            currSum = nums[i] + sumHelper(l,r,tmpNums)

            while(l < r and l >= 0 and r < len(tmpNums)):
                currSum = nums[i] + sumHelper(l,r,tmpNums)
                if(abs(currSum-target) < abs(closest-target)): closest = currSum

                if currSum == target: return currSum
                if currSum < target:
                    l += 1
                elif currSum > target:
                    r -= 1
                
        return closest
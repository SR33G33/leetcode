# 1470. Shuffle the Array

# Given the array nums consisting of 2n elements in the form [x 1 ,x 2 ,...,x n ,y 1 ,y 2 ,...,y n ] .
# Return the array in the form [x 1 ,y 1 ,x 2 ,y 2 ,...,x n ,y n ] .
# Example 1: Input: nums = [2,5,1,3,4,7], n = 3 Output: [2,3,5,4,1,7] Explanation: Since x 1 =2, x 2 =5, x 3 =1, y 1 =3, y 2 =4, y 3 =7 then the answer is [2,3,5,4,1,7].
# Example 2: Input: nums = [1,2,3,4,4,3,2,1], n = 4 Output: [1,4,2,3,3,2,4,1]
# Example 3: Input: nums = [1,1,2,2], n = 2 Output: [1,2,1,2] Constraints: 1 <= n <= 500 nums.length == 2n 1 <= nums[i] <= 10^3

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return

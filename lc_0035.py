# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        startIndex = 0
        endIndex = len(nums)-1
        middleIndex = 0

        while(startIndex <= endIndex):
            # print(nums[startIndex:endIndex+1])
            middleIndex = (endIndex + startIndex) // 2
            # print(middleIndex)
            if(target == nums[middleIndex]):
                return middleIndex
            elif(target < nums[middleIndex]):
                endIndex = middleIndex - 1
            else: startIndex = middleIndex + 1

        return startIndex
    
sol = Solution()
# Run test cases
print(sol.searchInsert([1, 3, 5, 6], 5))
print(sol.searchInsert([1, 3, 5, 6], 2))
print(sol.searchInsert([1, 3, 5, 6], 7))
print(sol.searchInsert([1, 3, 5, 6], 4))


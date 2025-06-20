# 26. Remove Duplicates from a Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

import heapq

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # last_num = {last non duplicate number, position}
        last_num = None
        dup_positions = []
        num_non_dup = 0

        for i in range(len(nums)):
            if(nums[i] == last_num):
                dup_positions.append(i)
            else:
                num_non_dup += 1
                last_num = nums[i]
                if(dup_positions):
                    # print("swapping")
                    self.swap(i, heapq.heappop(dup_positions), nums)
                    dup_positions.append(i)
                    heapq.heapify(dup_positions)
            print(nums)
            print(dup_positions)
        return num_non_dup


    def swap(self, x, y, nums):
        temp = nums[x]
        nums[x] = nums[y]
        nums[y] = temp
        return nums



sol = Solution()
print(sol.removeDuplicates([1,1,2]))
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

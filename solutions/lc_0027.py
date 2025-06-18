# 26. Remove Element

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

import heapq

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        back_ptr = len(nums)-1

        for i in range(len(nums)):
            if(i > back_ptr): continue
            if(nums[i] == val):
                while(back_ptr >= 0 and nums[back_ptr] == val): back_ptr -= 1
                if(back_ptr >= 0 and back_ptr > i):
                    self.swap(i, back_ptr, nums)
            print(nums)
            # print(back_ptr)
        return back_ptr + 1

    def swap(self, x, y, nums):
        temp = nums[x]
        nums[x] = nums[y]
        nums[y] = temp
        return nums

sol = Solution()
print(sol.removeElement([1,1,2], 1))
print(sol.removeElement([0,0,1,1,1,2,2,3,3,4], 1))

# 26. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

import heapq

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = len(haystack)
        b = len(needle)

        if(b > a): return -1


        for i in range(a - b + 1):
            # print(haystack[i:i+len(needle)])
            if(haystack[i:i+b] == needle):
                return i
        return -1

        # while haystack_pointer < len(haystack):
        # # for haystack_pointer in range(len(haystack)):
        #     # print(haystack[haystack_pointer:len(haystack)])

        #     if(haystack[haystack_pointer] == needle[0]):
        #         starting_points.append(haystack_pointer)
        #         heapq.heapify(starting_points)

        #     if(haystack[haystack_pointer] == needle[needle_pointer]): 
        #         if(needle_pointer == 0): heapq.heappop(starting_points)
        #         needle_pointer += 1
        #     else: 
        #         needle_pointer = 0
        #         if(starting_points):
        #             haystack_pointer = heapq.heappop(starting_points)-1
        #             # print(haystack_pointer)
        #     # print(haystack_pointer)

        #     if(needle_pointer >= len(needle)): return haystack_pointer-needle_pointer + 1
        #     haystack_pointer += 1

        # return -1

sol = Solution()
print(sol.strStr("sadbutsad", "sad"))
print(sol.strStr("leetcode", "leeto"))
print(sol.strStr("a", "a"))
print(sol.strStr("mississippi", "issip"))


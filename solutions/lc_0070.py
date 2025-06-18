# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a, 2) + int(b, 2)))[2:]
        

sol = Solution()
print(sol.addBinary(a = "11", b = "1"))
print(sol.addBinary(a = "1010", b = "1011"))


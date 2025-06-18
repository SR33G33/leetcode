# 20. Valid Parenthesis

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 == 1:
            return False
    
        paren_stack = []

        for char in s:
            if char == ")":
                if len(paren_stack) == 0 or paren_stack.pop() != "(":
                    return False
            elif char == "]":
                if len(paren_stack) == 0 or paren_stack.pop() != "[":
                    return False
            elif char == "}":
                if len(paren_stack) == 0 or paren_stack.pop() != "{":
                    return False
            else:
                paren_stack.append(char)
            # print(paren_stack)


        return (len(paren_stack) == 0)


sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([])"))
print(sol.isValid("]"))


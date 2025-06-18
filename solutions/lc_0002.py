# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addNumHelper(self, l1, l2, carry):
        l1_done = False
        l2_done = False
        
        if(l1 == None): l1_done = True
        if(l2 == None): l2_done = True
        if(l1_done and l2_done and carry == 0): return None

        digit = 0
        if(l1 != None): digit += l1.val
        if(l2 != None): digit += l2.val

        digit += carry

        carry = digit // 10
        digit = digit % 10

        next_l1 = l1.next if l1 else None
        next_l2 = l2.next if l2 else None

        return ListNode(digit, self.addNumHelper(next_l1, next_l2, carry))



    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        return self.addNumHelper(l1, l2, 0)
    



# Function to create a linked list from a Python list
def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Function to print a linked list as a Python list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


# Test case 1
l1 = [2, 4, 3]
l2 = [5, 6, 4]
list1 = create_linked_list(l1)
list2 = create_linked_list(l2)

solution = Solution()
output = solution.addTwoNumbers(list1, list2)
print("Output:", end=" ")
print_linked_list(output)

# Test case 2
l1 = [0]
l2 = [0]
list1 = create_linked_list(l1)
list2 = create_linked_list(l2)

output = solution.addTwoNumbers(list1, list2)
print("Output:", end=" ")
print_linked_list(output)

# Test case 3
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
list1 = create_linked_list(l1)
list2 = create_linked_list(l2)

output = solution.addTwoNumbers(list1, list2)
print("Output:", end=" ")
print_linked_list(output)
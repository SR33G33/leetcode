# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeListHelper(self, l1, l2):

        if not l1 or not l2:
            return l1 or l2
        
        smaller_val = None
        if(l1.val < l2.val):
            smaller_val = l1.val
            l1 = l1.next
        else: 
            smaller_val = l2.val
            l2 = l2.next

        return ListNode(smaller_val, self.mergeListHelper(l1, l2))

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        return self.mergeListHelper(list1, list2)
    



# Function to create a linked list from a Python list
def create_linked_list(arr):
    if(arr):
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    return None

# Function to print a linked list as a Python list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


# Test case 1
l1 = [1,2,4]
l2 = [1,3,4]

list1 = create_linked_list(l1)
list2 = create_linked_list(l2)

solution = Solution()
output = solution.mergeTwoLists(list1, list2)
print("Output:", end=" ")
print_linked_list(output)

# Test case 2
l1 = []
l2 = []
list1 = create_linked_list(l1)
list2 = create_linked_list(l2)

output = solution.mergeTwoLists(list1, list2)
print("Output:", end=" ")
print_linked_list(output)

# Test case 3
l1 = []
l2 = [0]
list1 = create_linked_list(l1)
list2 = create_linked_list(l2)

output = solution.mergeTwoLists(list1, list2)
print("Output:", end=" ")
print_linked_list(output)
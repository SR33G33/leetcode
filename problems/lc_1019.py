# 1019. Next Greater Node In Linked List

# You are given the head of a linked list with n nodes.
# For each node in the list, find the value of the next greater node .
# That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.
# Return an integer array answer where answer[i] is the value of the next greater node of the i th node ( 1-indexed ).
# If the i th node does not have a next greater node, set answer[i] = 0 .
# Example 1: Input: head = [2,1,5] Output: [5,5,0]
# Example 2: Input: head = [2,7,4,3,5] Output: [7,0,5,5,0] Constraints: The number of nodes in the list is n . 1 <= n <= 10 4 1 <= Node.val <= 10 9

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        return

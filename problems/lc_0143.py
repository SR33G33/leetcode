# 143. Reorder List

# You are given the head of a singly linked-list.
# The list can be represented as: L 0 → L 1 → … → L n - 1 → L n Reorder the list to be on the following form: L 0 → L n → L 1 → L n - 1 → L 2 → L n - 2 → … You may not modify the values in the list's nodes.
# Only nodes themselves may be changed.
# Example 1: Input: head = [1,2,3,4] Output: [1,4,2,3]
# Example 2: Input: head = [1,2,3,4,5] Output: [1,5,2,4,3] Constraints: The number of nodes in the list is in the range [1, 5 * 10 4 ] . 1 <= Node.val <= 1000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        return

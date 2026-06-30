# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre_node = None
        now_node = head
        stack = []
        while now_node.next != None:
            stack.append(now_node.val)
            pre_node = now_node
            now_node = now_node.next
        stack.append(now_node.val)
        
        result = None
        cnt = 0
        while stack:
            cnt += 1
            if cnt == n:
                stack.pop()
                continue
            now_node = ListNode(stack.pop())
            now_node.next = result
            result = now_node
        return result

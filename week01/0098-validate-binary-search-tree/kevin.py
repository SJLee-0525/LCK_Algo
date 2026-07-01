# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [[root, float('-inf'), float('inf')]]
        while stack:
            now, min_val, max_val = stack.pop()
            if now.left != None:
                if  min_val < now.left.val < now.val:
                    stack.append([now.left, min_val, now.val])
                else:
                    return False
            if now.right != None:
                if now.val < now.right.val < max_val:
                    stack.append([now.right, now.val, max_val])
                else:
                    return False
        return True
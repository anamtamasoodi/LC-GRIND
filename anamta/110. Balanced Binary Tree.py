# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxDepth(root: Optional[TreeNode]) -> int:
        if (not root):
            return 0
        else:
            return max(1+maxDepth(root.left), 1+maxDepth(root.right))

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if (root):
            if (abs(maxDepth(root.left)-maxDepth(root.right)) > 1 ):
                return False
            else:
                return (self.isBalanced(root.left) and self.isBalanced(root.right))

        else:
            return True

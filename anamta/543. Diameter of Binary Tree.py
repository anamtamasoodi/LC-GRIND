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
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if (not root):
            return 0
        else:
            return max(maxDepth(root.left)+maxDepth(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        


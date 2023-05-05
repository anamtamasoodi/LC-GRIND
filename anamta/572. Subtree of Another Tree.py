# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and q):
            if(p.val == q.val and (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))):
                return True

        elif (not p and not q):
            return True

        else:
            return False

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and q):
            if(p.val == q.val and (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))):
                return True

        elif (not p and not q):
            return True

        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if (root and subRoot and self.isSameTree(root, subRoot)):
            return True
        elif (not root and not subRoot):
            return True

        elif (not root):
            return False

        else:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))












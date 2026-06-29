# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        leftdepth = -1
        rightdepth = -1

        if root == None:
            return 0

        if root.right == None and root.left == None:
            return 1

        if root.left != None:
            leftdepth = self.maxDepth(root.left)
        if root.right != None:
            rightdepth = self.maxDepth(root.right)
        
        return rightdepth + 1 if rightdepth > leftdepth else leftdepth + 1

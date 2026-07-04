# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self) -> None:
        self.isBlcnd = True

    def subTreeHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.subTreeHeight(root.left)
        rightHeight = self.subTreeHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            self.isBlcnd = False

        return rightHeight + 1 if rightHeight > leftHeight else leftHeight + 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
            
        self.subTreeHeight(root)

        return self.isBlcnd


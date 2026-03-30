# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.checkValid(root, -1000, 1000)

    
    def checkValid(self, root: Optional[TreeNode], minVal, maxVal) -> bool:

        if not root:
            return True

        if minVal < root.val < maxVal:
            return self.checkValid(root.left, minVal , root.val) and self.checkValid(root.right, root.val, maxVal)
        
        return False

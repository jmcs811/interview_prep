# given a binary tree, determine wheter it is a binary search tree

class TreeNone:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root, lower=float('-inf'), upper=float('inf')):
        if not root:
            return True

        if root.val <= lower or root.val >= upper:
            return False

        return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)
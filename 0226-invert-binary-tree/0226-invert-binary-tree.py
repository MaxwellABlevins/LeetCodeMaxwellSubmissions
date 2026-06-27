# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        def walk(root):
            if not root:
                return

            root.left, root.right = root.right, root.left
            walk(root.left)
            walk(root.right)


        walk(root)
        return root
class Solution:
    def inorderTraversal(self, root) -> list[int]:
        if root is None:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
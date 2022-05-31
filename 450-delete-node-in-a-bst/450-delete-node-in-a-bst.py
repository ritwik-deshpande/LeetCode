# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_left_most(self, root, prev):
        
        if root is None:
            # print(prev)
            return prev
        
        if root.left is None and root.right is None:
            return root
        
        return self.get_left_most(root.left, root)
        
    def get_right_most(self, root, prev):
        
        if root is None:
            return prev
        
        if root.left is None and root.right is None:
            return root
        
        return self.get_right_most(root.right, root)
        
    
    def f(self, root, prev, val, pos):
        
        if root:
            if root.val == val:
                
                if pos == 'r':
                    left_tree = root.left
                    right_tree = root.right

                    if left_tree:
                        right_most_node = self.get_right_most(left_tree, left_tree)

                        right_most_node.right = right_tree

                        prev.right = left_tree
                    else:
                        prev.right = right_tree

                elif pos == 'l':
                    left_tree = root.left
                    right_tree = root.right

                    if right_tree:
                        left_most_node = self.get_left_most(right_tree, right_tree)

                        left_most_node.left = left_tree

                        prev.left = right_tree
                        
                    else:
                        prev.left = left_tree
                    
                else:
                    
                    if root.right:
                        self.root = root.right
                        # print(root.right)
                        left_most_node = self.get_left_most(root.right, root.right)
                        # print(left_most_node)
                        left_most_node.left = root.left
                        
                    elif root.left:
                        self.root = root.left
                    else:
                        self.root = None
                    
            elif root.val < val:
                self.f(root.right, root, val, 'r')
                
            else:
                self.f(root.left, root, val, 'l')
                    
                    
                
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        self.root = root
        
        self.f(root, root, key, '')
        
        return self.root
        
        
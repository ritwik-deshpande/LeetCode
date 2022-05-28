# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, nums):
        
        if len(nums) > 0:
            L = len(nums)
            mid = L//2
            root_val = nums[mid]
            root = TreeNode(0)
            root.val = root_val
            
            if mid < L:
            
                nums_left = nums[:mid]
                nums_right = nums[mid + 1 :]

                root.left = self.construct(nums_left)
                root.right = self.construct(nums_right)
            else:
                root.left = None
                root.right = None
            return root
        
        else:
            return None
            
            
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        return self.construct(nums)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, nums):
        
        L = len(nums)
        
        if L > 0:
            retval = []
            for i in range(L):


                op_l = self.construct(nums[:i])

                op_r = self.construct(nums[i + 1: ])

                for l_c in op_l:
                    for r_c in op_r:
                        root = TreeNode(nums[i])
                        root.left = l_c
                        root.right = r_c
                        retval.append(root)
                        
            return retval
        else:
            return [None]
                
            
            
            
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        return self.construct([ num + 1 for num in range(n)])
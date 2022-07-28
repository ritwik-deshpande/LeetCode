class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = self.constructST(nums, 0, len(nums) - 1)
        

    def update(self, index: int, val: int) -> None:
        self.updateValue(self.root, index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(self.root, left, right)
    
    
    def constructST(self, arr, l, r):
        
        if l == r:
            root = TreeNode(arr[l])
            root.left = None
            root.right = None
            root.range = [l, r]
            return root
            
        
        mid = (l + r)//2
        left_child = self.constructST(arr, l, mid)
        right_child = self.constructST(arr, mid + 1, r) 
        
        root = TreeNode(left_child.val + right_child.val)
        root.left = left_child
        root.right = right_child
        root.range = [l, r]
        
        return root
        
        
    def updateValue(self, root, idx, val):
        
        if root.range[0] <= idx and idx <= root.range[1]:
            
            if root.range[0] == idx and idx == root.range[1]:
                root.val = val
                return val
            
            v1 = self.updateValue(root.left, idx, val)
            v2 = self.updateValue(root.right, idx, val)
            root.val = v1 + v2
            return v1 + v2
            

        else:
            return root.val
        
    def getSum(self, root, l, r):
        
        
        if l > root.range[1] or r < root.range[0]:
            return 0
        
        if l <= root.range[0] and root.range[1] <= r:
            return root.val
            
        
        else:
            return self.getSum(root.left, l , r) + self.getSum(root.right, l ,r)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
class TreeNode:
    def __init__(self):
        self.map = collections.defaultdict(int)
        self.left = None
        self.right = None
        self.range = [] 

class RangeFreqQuery:
    
    def constructST(self, arr, l, r):
        
        if l == r:
            root = TreeNode()
            root.left = None
            root.right = None
            root.range = [l, r]
            root.map[arr[l]] += 1
            return root
            
        
        mid = (l + r)//2
        left_child = self.constructST(arr, l, mid)
        right_child = self.constructST(arr, mid + 1, r) 
        
        root = TreeNode()
        root.left = left_child
        root.right = right_child
        root.range = [l, r]
        for k, v in left_child.map.items():
            root.map[k] += v
            
        for k, v in right_child.map.items():
            root.map[k] += v
                    
        return root
    

    def __init__(self, arr: List[int]):
        
        self.root = self.constructST(arr, 0, len(arr) - 1)
        
    
    def getSum(self, root, l, r, k):
        
        
        if l > root.range[1] or r < root.range[0]:
            return 0
        
        if l <= root.range[0] and root.range[1] <= r:
            return root.map[k]
            
        
        else:
            return self.getSum(root.left, l , r, k) + self.getSum(root.right, l ,r, k)
        

    def query(self, left: int, right: int, value: int) -> int:
        
        return self.getSum(self.root, left, right, value)
        
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
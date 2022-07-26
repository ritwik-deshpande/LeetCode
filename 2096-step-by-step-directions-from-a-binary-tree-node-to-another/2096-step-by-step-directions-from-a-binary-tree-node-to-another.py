class Solution:
    resStart = ""
    resEnd = ""
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findCommonAncester(root, startValue, destValue) -> TreeNode:
            if not root:
                return None
            
            if root.val == startValue or root.val == destValue:
                return root
            
            left = findCommonAncester(root.left, startValue, destValue)
            right = findCommonAncester(root.right, startValue, destValue)
            
            return root if left and right else left or right
        
        def getStartDirection(root, start):
            if not root: 
                return False
            
            if root.val == start:
                return True
            
            left = getStartDirection(root.left, start)
            right = getStartDirection(root.right, start)
            
            if left or right:
                self.resStart += "U"
                return True
            
            return False
        
        def getDestDirection(root, end):
            if not root: 
                return False
            
            if root.val == end:
                return True
            
            left = getDestDirection(root.left, end)
            right = getDestDirection(root.right, end)
            
            if right and not left: 
                self.resEnd += "R"
                return True
            elif left and not right:
                self.resEnd += "L"
                return True
            return False
        
        node = findCommonAncester(root, startValue, destValue)
        getStartDirection(node, startValue)
        getDestDirection(node, destValue)
        print(self.resStart)
        print(self.resEnd)

        return self.resStart + self.resEnd[::-1]
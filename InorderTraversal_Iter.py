#This is Iterative Solution, using stack 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traverse=[]
        stack=[]
        CurrentNode=root

        while CurrentNode or stack:
            while CurrentNode:
                stack.append(CurrentNode)
                CurrentNode = CurrentNode.left
            CurrentNode = stack.pop()
            traverse.append(CurrentNode.val)
            CurrentNode=CurrentNode.right
        return traverse

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def isSymmetric(root):
    def isSameTree(left,right):  
        if not left and not right:
            return True
        if not left or not right:
            return False   
        return left.val==right.val and isSameTree(left.left,right.right) and isSameTree(left.right,right.left)
            
    return isSameTree(root.left,root.right)   
    
    
    
#root=TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(5)),TreeNode(2,TreeNode(3),TreeNode(5)))
#print(isSymmetric(root))
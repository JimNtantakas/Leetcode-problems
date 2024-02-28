# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):        
    def isSameTree(self,p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        """
        result1=result2=True
        if p.val!=q.val:
            return False
        
        if (p.left!=None) and (q.left!=None):
            result1=self.isSameTree(p.left,q.left)
        elif ((p.left!=None) or (q.left!=None)):
            result1=False
            
        if (p.right!=None) and (q.right!=None):
            result2=self.isSameTree(p.right,q.right)
        elif ((p.right!=None) or (q.right!=None)):
            result2=False
            
        if result1 and result2:
            return True
        return False
        """
        
        
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2))
solution_instance=Solution()
print(solution_instance.isSameTree(p,q))
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def inorderTraversal(self, root):
        if root is not None:
            if root.left==None and root.right==None:
                return [root.val]
            
            flag1=flag2=0
            if root.left!=None:        
                r1=self.inorderTraversal(root.left)
                flag1=1
            if root.right!=None:
                r2=self.inorderTraversal(root.right)
                flag2=1
            
            mylist=[]
            if flag1:
                for x in r1:
                    mylist.append(x)
            mylist.append(root.val)
            if flag2:
                for x in r2:
                    mylist.append(x)
            return mylist
            

"""
#root=TreeNode(1,None,TreeNode(2,TreeNode(3),TreeNode(4)))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
solution_instance=Solution()
print(solution_instance.inorderTraversal(root))
"""
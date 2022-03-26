class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

t=TreeNode(1)
t.left=TreeNode(-5)
t.left.left=TreeNode(1)
t.left.right=TreeNode(2)
t.right=TreeNode(3)
t.right.left=TreeNode(-4)
t.right.right=TreeNode(-5)

def findSubtree(root:TreeNode):
# write your code here

    if root is None:
        return 0
    else:

        left_score = findSubtree(root.left)
        right_score = findSubtree(root.right)
        r_score = findSubtree(root)

        return max(left_score,right_score,r_score)



print(findSubtree(l))


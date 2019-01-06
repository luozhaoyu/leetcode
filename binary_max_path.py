class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "%s: %s, %s" % (self.val, self.left, self.right)


class Solution:
    # @param root, a tree node
    # @res =  an integer
    def maxPathSum(self, root):
        if hasattr(root, 'max_two_path'):
            return root.max_two_path
        res = 0
        root.max = root.val
        if root.left and root.right:
            res = max(max(root.val, 0) + self.maxPathSum(root.left), max(root.val, 0) + self.maxPathSum(root.right), root.val + self.max_single_path(root.left) + self.max_single_path(root.right))
            root.max = max(root.left.max, root.right.max, root.max)
        elif not root.left and not root.right:
            res = root.val
            root.max = root.val
        elif root.left:
            res = max(self.maxPathSum(root.left), max(root.val, 0) + self.max_single_path(root.left))
            root.max = max(root.left.max, root.max)
        elif root.right:
            res = max(self.maxPathSum(root.right), max(root.val, 0) + self.max_single_path(root.right))
            root.max = max(root.right.max, root.max)
        res = max(res, root.max)
        root.max_two_path = res
        return res

    def max_single_path(self, root):
        if hasattr(root, 'max_one_path'):
            return root.max_one_path

        res = 0
        if root.left and root.right:
            res = root.val + max(self.max_single_path(root.left), self.max_single_path(root.right), 0)
        elif not root.left and not root.right:
            res = root.val
        elif root.left:
            res = root.val + max(self.max_single_path(root.left), 0)
        elif root.right:
            res = root.val + max(self.max_single_path(root.right), 0)
        root.max_one_path = res
        return res

s = Solution()
nodes = [TreeNode(i) for i in range(5)]
nodes[0].left = nodes[1]
nodes[0].right = nodes[3]
nodes[1].left = nodes[2]
nodes[3].left = nodes[4]
nodes[3].right = TreeNode(-3)

nodes[2].left = TreeNode(-1)
n_2 = TreeNode(-2)
n_2.left = TreeNode(-1)
print s.maxPathSum(nodes[0])
print s.maxPathSum(nodes[2])
print s.maxPathSum(TreeNode(-5))
print s.maxPathSum(n_2)

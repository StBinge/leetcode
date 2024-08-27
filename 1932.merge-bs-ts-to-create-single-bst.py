#
# @lc app=leetcode.cn id=1932 lang=python3
# @lcpr version=30204
#
# [1932] 合并多棵二叉搜索树
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        if len(trees) == 1:
            return trees[0]
        leaves_val = set()
        val2nodes = {}
        for tree in trees:
            if tree.left:
                leaves_val.add(tree.left.val)
            if tree.right:
                leaves_val.add(tree.right.val)
            val2nodes[tree.val] = tree

        root = None
        for tree in trees:
            if tree.val in leaves_val:
                continue
            if root:
                return None
            root = tree

        if not root:
            return None

        def dfs(node: TreeNode, mi, mx):
            if not node:
                return True
            if node.val <= mi or node.val >= mx:
                return False
            if not node.left and not node.right:
                nxt = val2nodes.pop(node.val, None)
                if not nxt:
                    return True
                node.left = nxt.left
                node.right = nxt.right
            if not dfs(node.left, mi, node.val):
                return False
            if not dfs(node.right, node.val, mx):
                return False
            return True

        if not dfs(root, 0, 10**5):
            return None

        return root if len(val2nodes) == 1 else None


# @lc code=end
trees = list(map(TreeNode.build, [[7]]))
assert Solution().canMerge(trees).to_str() == "[7]"
trees = list(map(TreeNode.build, [[10, 9], [9, 8], [8, 7]]))
assert Solution().canMerge(trees).to_str() == "[10,9,null,8,null,7]"

trees = list(map(TreeNode.build, ["[1,null,3]", [3, 1], [4, 2]]))
assert Solution().canMerge(trees) == None

trees = list(map(TreeNode.build, ["[2,null,5]", [3, 1, 4], "[1,null,2]"]))
assert Solution().canMerge(trees) == None

trees = list(map(TreeNode.build, [[3, 1], [1], [2, 1]]))
assert Solution().canMerge(trees) == None


trees = list(map(TreeNode.build, [[6, 4], [7, 6], "[5,null,7]"]))
assert Solution().canMerge(trees) == None

trees = list(map(TreeNode.build, [[5, 3, 8], [3, 2, 6]]))
assert Solution().canMerge(trees) == None


trees = list(map(TreeNode.build, [[2, 1], [3, 2, 5], [5, 4]]))
ret = Solution().canMerge(trees)
assert ret.to_str() == "[3,2,5,1,null,4]"

#
# @lcpr case=start
# [[2,1],[3,2,5],[5,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,3,8],[3,2,6]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,4],[3]]\n
# @lcpr case=end

#

#
# @lc app=leetcode.cn id=LCR 145 lang=python3
# @lcpr version=30204
#
# [LCR 145] 判断对称二叉树
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
    def checkSymmetricTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q=deque([root,root])
        while q:
            x=q.popleft()
            y=q.popleft()
            if (x and y and x.val==y.val):
                q.append(x.left)
                q.append(y.right)
                q.append(x.right)
                q.append(y.left)
            elif not x and not y:
                continue
            else:
                return False
        return True
# @lc code=end
assert not Solution().checkSymmetricTree(TreeNode.build('[1,2,2,null,3,null,3]'))
assert Solution().checkSymmetricTree(TreeNode.build([6,7,7,8,9,9,8]))


#
# @lcpr case=start
# [6,7,7,8,9,9,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#


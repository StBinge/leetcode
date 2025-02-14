#
# @lc app=leetcode.cn id=2641 lang=python3
# @lcpr version=30204
#
# [2641] 二叉树的堂兄弟节点 II
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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        q = [root]
        while q:
            temp=q
            q=[]
            nxt_sum=0
            for node in temp:
                if node.left:
                    nxt_sum+=node.left.val
                    q.append(node.left)
                if node.right:
                    nxt_sum+=node.right.val
                    q.append(node.right)

            for node in temp:
                child_sum=0
                if node.left:
                    child_sum+=node.left.val
                if node.right:
                    child_sum+=node.right.val
                if node.left:
                    node.left.val=nxt_sum-child_sum
                if node.right:
                    node.right.val=nxt_sum-child_sum
        return root



# @lc code=end
assert Solution().replaceValueInTree(TreeNode.build("[3,1,2]")).to_str() == "[0,0,0]"
assert (
    Solution().replaceValueInTree(TreeNode.build("[5,4,9,1,10,null,7]")).to_str()
    == "[0,0,0,7,7,null,11]"
)


#
# @lcpr case=start
# [5,4,9,1,10,null,7]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,2]\n
# @lcpr case=end

#

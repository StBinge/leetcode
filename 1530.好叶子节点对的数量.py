#
# @lc app=leetcode.cn id=1530 lang=python3
#
# [1530] 好叶子节点对的数量
#
from sbw import *


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ret = 0

        def traverse(node: TreeNode):
            if not node:
                return {}
            if not node.left and not node.right:
                return {0: 1}
            l_dis = traverse(node.left)
            r_dis = traverse(node.right)
            if l_dis and r_dis:
                nonlocal ret
                sorted_l_dis = sorted(l_dis.keys())
                sorted_r_dis = sorted(r_dis.keys())
                r_sum = sum(r_dis.values())
                ri = len(sorted_r_dis) - 1
                for ld in sorted_l_dis:
                    while ri >= 0:
                        rd = sorted_r_dis[ri]
                        if rd + ld + 2 > distance:
                            r_sum -= r_dis[rd]
                            ri -= 1
                        else:
                            break
                    if r_sum:
                        ret += l_dis[ld] * r_sum
                    else:
                        break
            tot = defaultdict(int)
            for k in l_dis:
                tot[k + 1] += l_dis[k]
            for k in r_dis:
                tot[k + 1] += r_dis[k]
            return tot

        traverse(root)
        return ret


# @lc code=end

assert Solution().countPairs(TreeNode.build("[78,15,81,73,98,36,null,30,null,63,32]"), 6) == 6
assert Solution().countPairs(TreeNode.build("[1,1,1]"), 2) == 1
assert Solution().countPairs(TreeNode.build("[100]"), 1) == 0
assert Solution().countPairs(TreeNode.build("[7,1,4,6,null,5,3,null,null,null,null,null,2]"), 3) == 1
assert Solution().countPairs(TreeNode.build("[1,2,3,4,5,6,7]"), 3) == 2
assert Solution().countPairs(TreeNode.build("[1,2,3,null,4]"), 3) == 1

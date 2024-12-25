#
# @lc app=leetcode.cn id=2476 lang=python3
# @lcpr version=30204
#
# [2476] 二叉搜索树最近节点查询
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
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        vals=[]
        def traverse(node:TreeNode):
            if not node:
                return
            traverse(node.left)
            vals.append(node.val)
            traverse(node.right)

        traverse(root)

        N=len(queries)
        # M=len(vals)
        ret=[None]*N
        sorted_ids=sorted(range(N),key=queries.__getitem__)
        idx=0
        for id in sorted_ids:
            q=queries[id]
            idx=bisect_left(vals,q,lo=idx)
            if idx==len(vals):
                ret[id]=[vals[idx-1],-1]
                continue
            if q==vals[idx]:
                ret[id]=[q,q]
                continue
            mi=-1 if idx==0 else vals[idx-1]
            mx=vals[idx]
            ret[id]=[mi,mx]
            
        return ret
# @lc code=end
assert Solution().closestNodes(TreeNode.build('[4,null,9]'),[3])==[[-1,4]]
assert Solution().closestNodes(TreeNode.build('[6,2,13,1,4,9,15,null,null,null,null,null,null,14]'),[2,5,16])==[[2,2],[4,6],[15,-1]]


#
# @lcpr case=start
# [6,2,13,1,4,9,15,null,null,null,null,null,null,14]\n[2,5,16]\n
# @lcpr case=end

# @lcpr case=start
# [4,null,9]\n[3]\n
# @lcpr case=end

#


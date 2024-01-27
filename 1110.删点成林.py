#
# @lc app=leetcode.cn id=1110 lang=python3
#
# [1110] 删点成林
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
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ret=[]
        deletes=set(to_delete)
        def dfs(node:TreeNode,has_root):
            if not node:
                return False
            removed=False
            if node.val in deletes:
                removed=True
            if not has_root and not removed:
                ret.append(node)
            if dfs(node.left,not removed):
                node.left=None
            if dfs(node.right,not removed):
                node.right=None
            return removed
        dfs(root,False)
        return ret
# @lc code=end
ans=Solution().delNodes(TreeNode.build('[1,2,4,null,3]'), to_delete = [3])
ret='[[1,2,4]]'
ret=eval_list_str(ret)
ret.sort(key=len)
ans=sorted([eval_list_str(node.to_str()) for node in ans],key=len)
assert ret==ans

ans=Solution().delNodes(TreeNode.build([1,2,3,4,5,6,7]), to_delete = [3,5])
ret='[[1,2,null,4],[6],[7]]'
ret=eval_list_str(ret)
ret.sort(key=len)
ans=sorted([eval_list_str(node.to_str()) for node in ans],key=len)
assert ret==ans

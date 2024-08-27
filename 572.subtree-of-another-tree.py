#
# @lc app=leetcode.cn id=572 lang=python3
# @lcpr version=30204
#
# [572] 另一棵树的子树
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def convert(node:TreeNode,vals:list):
            if not node:
                vals.append(10**5)
                return
            convert(node.left,vals)
            vals.append(node.val)
            convert(node.right,vals)
        
        root_vals=[]
        convert(root,root_vals)
        sub_vals=[]
        convert(subRoot,sub_vals)

        j=0
        N=len(sub_vals)
        nxt=[0]*N
        for i in range(1,N):
            while j and sub_vals[i]!=sub_vals[j]:
                j=nxt[j]
            if sub_vals[j]==sub_vals[i]:
                j+=1
            nxt[i]=j
        
        j=0
        for i in range(len(root_vals)):
            while j and sub_vals[j]!=root_vals[i]:
                j=nxt[j-1]
            if sub_vals[j]==root_vals[i]:
                j+=1
                if j==N:
                    return True
        return False


# @lc code=end
assert Solution().isSubtree(TreeNode.build('[1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]'),TreeNode.build('[1,null,1,null,1,null,1,null,1,null,1,2]'))==True
assert Solution().isSubtree(TreeNode.build('[3,4,5,1,null,2]'),TreeNode.build([3,1,2]))==False


#
# @lcpr case=start
# [3,4,5,1,2]\n[4,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,2,null,null,null,null,0]\n[4,1,2]\n
# @lcpr case=end

#


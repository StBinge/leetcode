#
# @lc app=leetcode.cn id=2196 lang=python3
# @lcpr version=30204
#
# [2196] 根据描述创建二叉树
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
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes=defaultdict(TreeNode)
        vals=set()
        for p,c,left in descriptions:
            if left:
                nodes[p].left=nodes[c]
            else:
                nodes[p].right=nodes[c]
            vals.add(c)
        
        for v,node in nodes.items():
            node.val=v
        
        for v in nodes:
            if v not in vals:
                return nodes[v]



# @lc code=end
def check(args,ans):
    ret = Solution().createBinaryTree(args)
    assert ret.to_str().replace(' ','')==str(ans).replace(' ','')

check( [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]],[50,20,80,15,17,19])


#
# @lcpr case=start
# [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,1],[2,3,0],[3,4,1]]\n
# @lcpr case=end

#


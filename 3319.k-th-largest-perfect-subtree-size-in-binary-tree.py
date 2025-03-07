#
# @lc app=leetcode.cn id=3319 lang=python3
# @lcpr version=30204
#
# [3319] 第 K 大的完美二叉子树的大小
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        h=[]
        def dfs(node:TreeNode):
            if not node:
                return 0
            l_h=dfs(node.left)
            r_h=dfs(node.right)
            if l_h!=-1 and l_h==r_h:
                heapq.heappush(h,l_h+1)
                if len(h)>k:
                    heapq.heappop(h)
                return l_h+1
            return -1
        dfs(root)
        return 2**h[0]-1 if len(h)>=k else -1
# @lc code=end
assert Solution().kthLargestPerfectSubtree( TreeNode.build('[1,2,3,null,4]'), k = 3)==-1
assert Solution().kthLargestPerfectSubtree( TreeNode.build(' [1,2,3,4,5,6,7]'), k = 1)==7
assert Solution().kthLargestPerfectSubtree( TreeNode.build('[5,3,6,5,2,5,7,1,8,null,null,6,8]'), k = 2)==3


#
# @lcpr case=start
# [5,3,6,5,2,5,7,1,8,null,null,6,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,null,4]\n3\n
# @lcpr case=end

#


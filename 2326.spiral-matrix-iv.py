#
# @lc app=leetcode.cn id=2326 lang=python3
# @lcpr version=30204
#
# [2326] 螺旋矩阵 IV
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ret = [[-1] * n for _ in range(m)]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir=0
        r,c=0,-1
        while head:
            nr, nc = r + dirs[dir][0], c + dirs[dir][1]
            if 0 <= nr < m and 0 <= nc < n and ret[nr][nc] == -1:
                ret[nr][nc]=head.val
                head=head.next
                r,c=nr,nc
            else:
                dir=(dir+1)%4
        
        return ret


# @lc code=end
assert Solution().spiralMatrix(m = 3, n = 5, head = ListNode.build([3,0,2,6,8,1,7,9,4,2,5,5,0]))==[[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]

#
# @lcpr case=start
# 3\n5\n[3,0,2,6,8,1,7,9,4,2,5,5,0]\n
# @lcpr case=end

# @lcpr case=start
# 1\n4\n[0,1,2]\n
# @lcpr case=end

#

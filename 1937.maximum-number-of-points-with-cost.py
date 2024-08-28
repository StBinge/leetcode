#
# @lc app=leetcode.cn id=1937 lang=python3
# @lcpr version=30204
#
# [1937] 扣分后的最大得分
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        R, C = len(points), len(points[0])
        for i in range(1, R):
 
            right_max=[0]*(C+1)
            right_max[-1]=float('-inf')
            for j in range(C-1,-1,-1):
                right_max[j]=max(right_max[j+1],points[i-1][j]-j)
  
            left_max=0
            for j in range(C):
                l_max=left_max-j
                r_max=right_max[j]+j
                points[i][j]+=max(l_max,r_max)
                left_max=max(left_max,points[i-1][j]+j)
        return max(points[-1])


# @lc code=end
assert Solution().maxPoints([[2,2],[2,2],[2,2]]) == 6
assert Solution().maxPoints([[1, 5], [2, 3], [4, 2]]) == 11
assert Solution().maxPoints([[1, 2, 3], [1, 5, 1], [3, 1, 1]]) == 9


#
# @lcpr case=start
# [[1,2,3],[1,5,1],[3,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,5],[2,3],[4,2]]\n
# @lcpr case=end

#

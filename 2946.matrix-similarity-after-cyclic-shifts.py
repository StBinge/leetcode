#
# @lc app=leetcode.cn id=2946 lang=python3
# @lcpr version=30204
#
# [2946] 循环移位后的矩阵相似检查
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        C = len(mat[0])
        k%=C

        return k==0 or all(row==row[k:]+row[:k] for row in mat)


# @lc code=end
assert Solution().areSimilar(mat=[[1, 2]], k=1) == False
assert Solution().areSimilar(mat=[[2, 2], [2, 2]], k=3)
assert Solution().areSimilar(mat=[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], k=2)


#
# @lcpr case=start
# [[1,2,1,2],[5,5,5,5],[6,3,6,3]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[2,2],[2,2]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,2]]\n1\n
# @lcpr case=end

#

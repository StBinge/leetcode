#
# @lc app=leetcode.cn id=2545 lang=python3
# @lcpr version=30204
#
# [2545] 根据第 K 场考试的分数排序
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda x:x[k],reverse=True)
        return score
# @lc code=end



#
# @lcpr case=start
# [[10,6,9,1],[7,5,11,2],[4,8,3,15]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[3,4],[5,6]]\n0\n
# @lcpr case=end

#


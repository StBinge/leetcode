#
# @lc app=leetcode.cn id=LCR 172 lang=python3
# @lcpr version=30204
#
# [LCR 172] 统计目标成绩的出现次数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        left=bisect_left(scores,target)
        right=bisect_right(scores,target,lo=left)
        return right-left
# @lc code=end



#
# @lcpr case=start
# [2, 2, 3, 4, 4, 4, 5, 6, 6, 8]\n4\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 3, 5, 7, 9]\n6\n
# @lcpr case=end

#


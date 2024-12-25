#
# @lc app=leetcode.cn id=2244 lang=python3
# @lcpr version=30204
#
# [2244] 完成所有任务需要的最少轮数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt=Counter(tasks)
        if any(v==1 for v in cnt.values()):
            return -1
        return sum((v-1)//3+1 for v in cnt.values())

# @lc code=end



#
# @lcpr case=start
# [2,2,3,3,2,4,4,4,4,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,3]\n
# @lcpr case=end

#


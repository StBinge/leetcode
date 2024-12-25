#
# @lc app=leetcode.cn id=2141 lang=python3
# @lcpr version=30204
#
# [2141] 同时运行 N 台电脑的最长时间
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)
        s=sum(batteries)
        for b in batteries:
            if b>s//n:
                s-=b
                n-=1
            else:
                return s//n
        


# @lc code=end
assert Solution().maxRunTime(3,[10,10,3,5])==8
assert Solution().maxRunTime(n = 2, batteries = [3,3,3])==4
assert Solution().maxRunTime(n = 2, batteries = [1,1,1,1])==2


#
# @lcpr case=start
# 2\n[3,3,3]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,1,1,1]\n
# @lcpr case=end

#


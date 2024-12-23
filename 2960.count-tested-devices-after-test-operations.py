#
# @lc app=leetcode.cn id=2960 lang=python3
# @lcpr version=30204
#
# [2960] 统计已测试设备
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ret=0
        for b in batteryPercentages:
            if b>ret:
                ret+=1
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,1,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2]\n
# @lcpr case=end

#


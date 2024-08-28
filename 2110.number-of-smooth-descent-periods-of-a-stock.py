#
# @lc app=leetcode.cn id=2110 lang=python3
# @lcpr version=30204
#
# [2110] 股票平滑下跌阶段的数目
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ret=1
        cnt=1
        for right in range(1,len(prices)):
            if prices[right]!=prices[right-1]-1:
                cnt=1
            else:
                cnt+=1
            ret+=cnt

        return ret
# @lc code=end



#
# @lcpr case=start
# [3,2,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [8,6,7,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#


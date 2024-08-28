#
# @lc app=leetcode.cn id=2125 lang=python3
# @lcpr version=30204
#
# [2125] 银行中的激光束数量
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        N=len(bank)
        ret=0
        pre=0
        for i in range(N):
            cur=bank[i].count('1')
            if cur==0:
                continue
            ret+=pre*cur
            pre=cur
        return ret
# @lc code=end



#
# @lcpr case=start
# ["011001","000000","010100","001000"]\n
# @lcpr case=end

# @lcpr case=start
# ["000","111","000"]\n
# @lcpr case=end

#


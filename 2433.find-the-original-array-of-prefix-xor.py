#
# @lc app=leetcode.cn id=2433 lang=python3
# @lcpr version=30204
#
# [2433] 找出前缀异或的原始数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ret=pref.copy()
        for i in range(1,len(pref)):
            ret[i]^=pref[i-1]
        return ret
# @lc code=end



#
# @lcpr case=start
# [5,2,0,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [13]\n
# @lcpr case=end

#


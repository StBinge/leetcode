#
# @lc app=leetcode.cn id=2496 lang=python3
# @lcpr version=30204
#
# [2496] 数组中字符串的最大值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ret=0
        for s in strs:
            if s.isnumeric():
                ret=max(ret,int(s))
            else:
                ret=max(ret,len(s))
        return ret
# @lc code=end



#
# @lcpr case=start
# ["alic3","bob","3","4","00000"]\n
# @lcpr case=end

# @lcpr case=start
# ["1","01","001","0001"]\n
# @lcpr case=end

#


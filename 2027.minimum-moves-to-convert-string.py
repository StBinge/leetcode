#
# @lc app=leetcode.cn id=2027 lang=python3
# @lcpr version=30204
#
# [2027] 转换字符串的最少操作次数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumMoves(self, s: str) -> int:
        ret=0
        idx=0
        N=len(s)
        while idx<N:
            if s[idx]=='X':
                idx+=3
                ret+=1
            else:
                idx+=1
        return ret
        
# @lc code=end



#
# @lcpr case=start
# "XXX"\n
# @lcpr case=end

# @lcpr case=start
# "XXOX"\n
# @lcpr case=end

# @lcpr case=start
# "OOOO"\n
# @lcpr case=end

#


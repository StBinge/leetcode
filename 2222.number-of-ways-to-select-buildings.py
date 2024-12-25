#
# @lc app=leetcode.cn id=2222 lang=python3
# @lcpr version=30204
#
# [2222] 选择建筑的方案数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros=s.count('0')
        ones=s.count('1')
        pre_zero=pre_one=0
        ret=0
        for ch in s:
            if ch=='0':
                ret+=pre_one*ones
                pre_zero+=1
                zeros-=1
            else:
                ret+=pre_zero*zeros
                pre_one+=1
                ones-=1
        return ret
# @lc code=end



#
# @lcpr case=start
# "001101"\n
# @lcpr case=end

# @lcpr case=start
# "11100"\n
# @lcpr case=end

#


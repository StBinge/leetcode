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
        N=len(s)
        ones=s.count('1')
        zeros=N-ones
        ret=0
        left_ones=left_zeros=0
        for ch in s:
            if ch=='1':
                left_ones+=1
                ret+=left_zeros*(zeros-left_zeros)
            else:
                left_zeros+=1
                ret+=left_ones*(ones-left_ones)
        return ret
# @lc code=end
assert Solution().numberOfWays('111000')==0
assert Solution().numberOfWays('001101')==6


#
# @lcpr case=start
# "001101"\n
# @lcpr case=end

# @lcpr case=start
# "11100"\n
# @lcpr case=end

#


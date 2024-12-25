#
# @lc app=leetcode.cn id=2427 lang=python3
# @lcpr version=30204
#
# [2427] 公因子的数目
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ret=0
        for i in range(1,min(a,b)+1):
            ret+=a%i==0 and b%i==0
        return ret
        
# @lc code=end



#
# @lcpr case=start
# 12\n6\n
# @lcpr case=end

# @lcpr case=start
# 25\n30\n
# @lcpr case=end

#


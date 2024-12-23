#
# @lc app=leetcode.cn id=2520 lang=python3
# @lcpr version=30204
#
# [2520] 统计能整除数字的位数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countDigits(self, num: int) -> int:
        x=num
        ret=0
        while x:
            x,d=divmod(x,10)
            ret+=num%d==0
        return ret
        
# @lc code=end
assert Solution().countDigits(7)==1


#
# @lcpr case=start
# 7\n
# @lcpr case=end

# @lcpr case=start
# 121\n
# @lcpr case=end

# @lcpr case=start
# 1248\n
# @lcpr case=end

#


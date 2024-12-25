#
# @lc app=leetcode.cn id=2160 lang=python3
# @lcpr version=30204
#
# [2160] 拆分数位后四位数字的最小和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:
        digits=[]
        while num:
            num,m=divmod(num,10)
            digits.append(m)
        digits.sort()
        return 10*(digits[0]+digits[1])+digits[2]+digits[3]

# @lc code=end
assert Solution().minimumSum(2239)==52


#
# @lcpr case=start
# 2932\n
# @lcpr case=end

# @lcpr case=start
# 4009\n
# @lcpr case=end

#


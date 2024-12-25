#
# @lc app=leetcode.cn id=2165 lang=python3
# @lcpr version=30204
#
# [2165] 重排数字的最小值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestNumber(self, num: int) -> int:
        neg=False
        if num<0:
            neg=True
            num=-num
        digits=list(str(num))
        digits.sort()
        if neg:
            return -int(''.join(digits[::-1]))
        
        for i in range(len(digits)):
            if digits[i]!='0':
                digits[i],digits[0]=digits[0],digits[i]
                break
        return int(''.join(digits))
    
# @lc code=end



#
# @lcpr case=start
# 310\n
# @lcpr case=end

# @lcpr case=start
# -7605\n
# @lcpr case=end

#


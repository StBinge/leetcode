#
# @lc app=leetcode.cn id=2535 lang=python3
# @lcpr version=30204
#
# [2535] 数组元素和与数字和的绝对差
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=ss=0
        for n in nums:
            s+=n
            ss+=sum(map(int,str(n)))
        return abs(s-ss)
# @lc code=end



#
# @lcpr case=start
# [1,15,6,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

#


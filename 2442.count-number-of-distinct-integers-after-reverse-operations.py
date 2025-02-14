#
# @lc app=leetcode.cn id=2442 lang=python3
# @lcpr version=30204
#
# [2442] 反转之后不同整数的数目
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s=set(nums)
        s.update(map(lambda n:int(str(n)[::-1]),list(s)))
        return len(s)
# @lc code=end



#
# @lcpr case=start
# [1,13,10,12,31]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2]\n
# @lcpr case=end

#


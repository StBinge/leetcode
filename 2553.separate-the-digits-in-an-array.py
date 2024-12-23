#
# @lc app=leetcode.cn id=2553 lang=python3
# @lcpr version=30204
#
# [2553] 分割数组中数字的数位
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ret=[]
        for n in nums:
            ret.extend(map(int,str(n)))
        return ret
# @lc code=end



#
# @lcpr case=start
# [13,25,83,77]\n
# @lcpr case=end

# @lcpr case=start
# [7,1,3,9]\n
# @lcpr case=end

#


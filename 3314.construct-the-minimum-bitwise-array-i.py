#
# @lc app=leetcode.cn id=3314 lang=python3
# @lcpr version=30204
#
# [3314] 构造最小位运算数组 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ret=[]
        for n in nums:
            if n&1==0:
                ret.append(-1)
                continue
            t=~n
            ret.append(n^((t&-t)>>1))
        return ret
# @lc code=end
assert Solution().minBitwiseArray([47])==[39]
assert Solution().minBitwiseArray([11,13,31])==[9,12,15]
assert Solution().minBitwiseArray([2,3,5,7])==[-1,1,4,3]


#
# @lcpr case=start
# [2,3,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [11,13,31]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=3309 lang=python3
# @lcpr version=30204
#
# [3309] 连接二进制表示可形成的最大数值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cmp_to_key
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        def cmp(x:int,y:int):
            return ((x<<y.bit_length())|y) - ((y<<x.bit_length())|x)
        
        nums.sort(key=cmp_to_key(cmp),reverse=True)

        ret=0
        for n in nums:
            ret=(ret<<n.bit_length())|n
        return ret

        
# @lc code=end
assert Solution().maxGoodNumber([2,91,119])==61294
assert Solution().maxGoodNumber([1,2,3])==30


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,8,16]\n
# @lcpr case=end

#


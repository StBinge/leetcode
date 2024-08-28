#
# @lc app=leetcode.cn id=1814 lang=python3
#
# [1814] 统计一个数组中好对子的数目
#
from sbw import *
# @lc code=start
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        counter=defaultdict(int)
        ret=0
        for x in nums:
            rev=0
            _x=x
            while x:
                rev=rev*10+x%10
                x//=10
            dif=_x-rev
            ret+=counter[dif]
            counter[dif]+=1
            ret%=10**9+7
        return ret

# @lc code=end
assert Solution().countNicePairs(nums = [13,10,35,24,76])==4
assert Solution().countNicePairs([42,11,1,97])

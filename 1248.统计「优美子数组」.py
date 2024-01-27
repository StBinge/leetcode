#
# @lc app=leetcode.cn id=1248 lang=python3
#
# [1248] 统计「优美子数组」
#
from sbw import *
# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # L=len(nums)
        cnt=0
        memo={0:1}
        ret=0
        for n in nums:
            cnt+=n%2
            pair=cnt-k
            ret+=memo.get(pair,0)
            memo[cnt]=memo.get(cnt,0)+1
        return ret
# @lc code=end
assert Solution().numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)==16
assert Solution().numberOfSubarrays(nums = [2,4,6], k = 1)==0
assert Solution().numberOfSubarrays(nums = [2,4,6], k = 1)==0

#
# @lc app=leetcode.cn id=2845 lang=python3
# @lcpr version=30204
#
# [2845] 统计趣味子数组的数目
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        cache=defaultdict(int)
        cache[0]=1
        cnt=0
        ret=0
        for i,n in enumerate(nums):
            cnt+=(n%modulo)==k
            ret+=cache[(cnt-k)%modulo]
            cache[cnt%modulo]+=1
        return ret
# @lc code=end
assert Solution().countInterestingSubarrays([11,12,21,31],10,1)==5
assert Solution().countInterestingSubarrays(nums = [3,1,9,6], modulo = 3, k = 0)==2
assert Solution().countInterestingSubarrays(nums = [3,2,4], modulo = 2, k = 1)==3


#
# @lcpr case=start
# [3,2,4]\n2\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,1,9,6]\n3\n0\n
# @lcpr case=end

#


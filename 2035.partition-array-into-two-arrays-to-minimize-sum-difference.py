#
# @lc app=leetcode.cn id=2035 lang=python3
# @lcpr version=30204
#
# [2035] 将数组分成两个数组并最小化数组和的差
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N=len(nums)
        S=sum(nums)
        half=N//2
        ret=float('inf')
        def pick(idx,cnt,pre):
            if cnt==0:
                nonlocal ret
                ret=min(ret,abs(2*pre-S))
                return
            if idx==N:
                return
            pick(idx+1,cnt-1,pre+nums[idx])
            pick(idx+1,cnt,pre)
        
        pick(0,half,0)
        return ret
# @lc code=end
assert Solution().minimumDifference([3,9,7,3])==2


#
# @lcpr case=start
# [3,9,7,3]\n
# @lcpr case=end

# @lcpr case=start
# [-36,36]\n
# @lcpr case=end

# @lcpr case=start
# [2,-1,0,4,-2,-9]\n
# @lcpr case=end

#


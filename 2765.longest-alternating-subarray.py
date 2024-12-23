#
# @lc app=leetcode.cn id=2765 lang=python3
# @lcpr version=30204
#
# [2765] 最长交替子数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ret=-1
        idx=1
        N=len(nums)
        while idx<N:
            if nums[idx-1]+1!=nums[idx]:
                idx+=1
                continue
            idx+=1
            cnt=2
            while idx<N and nums[idx]==nums[idx-2]:
                cnt+=1
                idx+=1
            ret=max(ret,cnt)
        return ret
# @lc code=end
assert Solution().alternatingSubarray([2,3,4,3,4])==4
assert Solution().alternatingSubarray([21,9,5])==-1


#
# @lcpr case=start
# [2,3,4,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6]\n
# @lcpr case=end

#


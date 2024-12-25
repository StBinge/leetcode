#
# @lc app=leetcode.cn id=2670 lang=python3
# @lcpr version=30204
#
# [2670] 找出不同元素数目差数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        N=len(nums)
        suf_cnt=[0]*(N)
        s=set()
        for i in range(N-1,-1,-1):
            suf_cnt[i]=len(s)
            s.add(nums[i])
        ret=[]
        s.clear()
        for i in range(N):
            s.add(nums[i])
            ret.append(len(s)-suf_cnt[i])
        return ret
# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3,4,2]\n
# @lcpr case=end

#


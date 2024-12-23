#
# @lc app=leetcode.cn id=2420 lang=python3
# @lcpr version=30204
#
# [2420] 找到所有好下标
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        N=len(nums)
        asec=[1]*N
        for i in range(N-2,k-1,-1):
            if nums[i]<=nums[i+1]:
                asec[i]+=asec[i+1]
        desc=1
        ret=[]
        for i in range(1,N-k):
            if desc>=k and asec[i+1]>=k:
                ret.append(i)
            if nums[i]<=nums[i-1]:
                desc+=1
            else:
                desc=1
        return ret
# @lc code=end
assert Solution().goodIndices([878724,201541,179099,98437,35765,327555,475851,598885,849470,943442],4)==[4,5]
assert Solution().goodIndices(nums = [2,1,1,2], k = 2)==[]
assert Solution().goodIndices(nums = [2,1,1,1,3,4,1], k = 2)==[2,3]


#
# @lcpr case=start
# [2,1,1,1,3,4,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,1,1,2]\n2\n
# @lcpr case=end

#


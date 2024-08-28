#
# @lc app=leetcode.cn id=3152 lang=python3
# @lcpr version=30204
#
# [3152] 特殊数组 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        N=len(nums)
        f=[1]*N
        for i in range(1,N):
            if (nums[i]^nums[i-1])&1:
                f[i]+=f[i-1]
        ret=[]
        for l,r in queries:

            ret.append(f[r]>r-l)
            
        return ret
# @lc code=end
assert Solution().isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]])==[False,True]
assert Solution().isArraySpecial(nums = [3,4,1,2,6], queries = [[0,4]])==[False]


#
# @lcpr case=start
# [3,4,1,2,6]\n[[0,4]]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,1,6]\n[[0,2],[2,3]]\n
# @lcpr case=end

#


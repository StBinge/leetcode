#
# @lc app=leetcode.cn id=面试题 16.17 lang=python3
# @lcpr version=30204
#
# [面试题 16.17] 连续数列
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # define item
        # [isum,lsum,rsum,mxsum]
        def merge(left,right):
            isum=left[0]+right[0]
            lsum=max(left[0]+right[1],left[1])
            rsum=max(right[2],left[2]+right[0])
            msum=max(left[2]+right[1],left[3],right[3])
            return [isum,lsum,rsum,msum]
        
        def query(l,r):
            if l==r:
                return [nums[l]]*4
            mid=(l+r)>>1
            left=query(l,mid)
            right=query(mid+1,r)
            return merge(left,right)
        
        return query(0,len(nums)-1)[3]
# @lc code=end

assert Solution().maxSubArray([-2])==-2
assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])==6

#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=2161 lang=python3
# @lcpr version=30204
#
# [2161] 根据给定数字划分数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        N=len(nums)
        ret=[pivot]*N
        l,r=0,N-1
        for n in nums:
            if n<pivot:
                ret[l]=n
                l+=1
            elif n>pivot:
                ret[r]=n
                r-=1
        l,r=r+1,N-1
        while l<r:
            ret[l],ret[r]=ret[r],ret[l]
            l+=1
            r-=1
        return ret

# @lc code=end
assert Solution().pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10)==[9,5,3,10,10,12,14]


#
# @lcpr case=start
# [9,12,5,10,14,3,10]\n10\n
# @lcpr case=end

# @lcpr case=start
# [-3,4,3,2]\n2\n
# @lcpr case=end

#


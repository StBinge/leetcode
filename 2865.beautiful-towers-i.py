#
# @lc app=leetcode.cn id=2865 lang=python3
# @lcpr version=30204
#
# [2865] 美丽塔 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        left=[[-1,-1]]
        rm_left=[0]
        for i,h in enumerate(heights):
            rm=0
            cur=i
            while h<=left[-1][0]:
                pre_h,idx=left.pop()
                rm+=(pre_h-h)*(cur-idx)
                cur=idx
            left.append([h,cur])
            rm_left.append(rm+rm_left[-1])
        
        N=len(heights)
        right=[[-1,N]]
        rm_right=0
        ret=float('inf')
        for i in range(N-1,-1,-1):
            rm=0
            h=heights[i]
            cur=i
            while h<=right[-1][0]:
                pre_h,idx=right.pop()
                rm+=(pre_h-h)*(idx-cur)
                cur=idx
            right.append([h,cur])
            rm_right+=rm
            ret=min(ret,rm_right+rm_left[i+1])
        
        return sum(heights)-ret
        
# @lc code=end
assert Solution().maximumSumOfHeights([6,5,3,9,2,7])==22


#
# @lcpr case=start
# [5,3,4,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [6,5,3,9,2,7]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,5,5,2,3]\n
# @lcpr case=end

#


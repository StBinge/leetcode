#
# @lc app=leetcode.cn id=2106 lang=python3
# @lcpr version=30204
#
# [2106] 摘水果
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        def is_valid(left,right):
            left_pos=fruits[left][0]
            left_step=abs(startPos-left_pos)
            right_pos=fruits[right][0]
            right_step=abs(right_pos-startPos)
            return \
                (right_pos<=startPos and left_step<=k) or \
                (left_pos>=startPos and right_step<=k) or \
                (left_step+right_step+min(left_step,right_step))<=k
        N=len(fruits)
        left=0
        ret=0
        s=0
        for right in range(N):
            s+=fruits[right][1]
            while left<=right and not is_valid(left,right):
                s-=fruits[left][1]
                left+=1
            ret=max(ret,s)
        return ret

# @lc code=end
assert Solution().maxTotalFruits(fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4)==14
assert Solution().maxTotalFruits([[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]],21,30)==71
assert Solution().maxTotalFruits(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4)==9


#
# @lcpr case=start
# [[2,8],[6,3],[8,6]]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [[0,3],[6,4],[8,5]]\n3\n2\n
# @lcpr case=end

#


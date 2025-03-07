#
# @lc app=leetcode.cn id=3281 lang=python3
# @lcpr version=30204
#
# [3281] 范围内整数的最大得分
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        N=len(start)

        def check(x):
            pre=float('-inf')
            for s in start:
                pre=max(pre+x,s)
                if pre>s+d:
                    return False
            return True
                

        left=0
        right=(start[-1]+d-start[0])//(N-1)
        ret=0
        while left<=right:
            mid=(left+right)>>1
            if check(mid):
                ret=mid
                left=mid+1
            else:
                right=mid-1
        return ret
        
# @lc code=end

assert Solution().maxPossibleScore( start = [2,6,13,13], d = 5)==5
assert Solution().maxPossibleScore(start = [6,0,3], d = 2)==4

#
# @lcpr case=start
# [6,0,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,6,13,13]\n5\n
# @lcpr case=end

#


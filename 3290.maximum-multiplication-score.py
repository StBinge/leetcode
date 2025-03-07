#
# @lc app=leetcode.cn id=3290 lang=python3
# @lcpr version=30204
#
# [3290] 最高乘法得分
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        f=[float('-inf')]*5
        f[0]=0

        for x in b:
            for i in range(3,-1,-1):
                f[i+1]=max(f[i+1],f[i]+x*a[i])
        return f[-1]
# @lc code=end
assert Solution().maxScore(a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4])==-1
assert Solution().maxScore( a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7])==26


#
# @lcpr case=start
# [3,2,5,6]\n[2,-6,4,-5,-3,2,-7]\n
# @lcpr case=end

# @lcpr case=start
# [-1,4,5,-2]\n[-5,-1,-3,-2,-4]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=2218 lang=python3
# @lcpr version=30204
#
# [2218] 从栈中取出 K 个硬币的最大面值和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        f0=[0]*(k+1)
        # f1=[0]*(k+1)
        cnt=0
        for pile in piles:
            N=len(pile)
            cnt+=N
            presums=list(accumulate(pile,initial=0))
            for i in range(min(cnt,k),0,-1):
                for j in range(min(i+1,N+1)):
                    f0[i]=max(f0[i],presums[j]+f0[i-j])
        return f0[-1]

# @lc code=end
assert Solution().maxValueOfCoins([[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]],9)==494
assert Solution().maxValueOfCoins(piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7)==706
assert Solution().maxValueOfCoins(piles = [[1,100,3],[7,8,9]], k = 2)==101


#
# @lcpr case=start
# [[1,100,3],[7,8,9]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]\n7\n
# @lcpr case=end

#


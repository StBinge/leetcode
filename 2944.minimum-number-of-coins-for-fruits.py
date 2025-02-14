#
# @lc app=leetcode.cn id=2944 lang=python3
# @lcpr version=30204
#
# [2944] 购买水果需要的最少金币数
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        N = len(prices)
        q=deque([((N+1,0))])
        for i in range(N,0,-1):
            while q[-1][0]>2*i+1:
                q.pop()
            f=prices[i-1]+q[-1][1]
            while f<=q[0][1]:
                q.popleft()
            q.appendleft((i,f))
        return q[0][1]


# @lc code=end
assert (
    Solution().minimumCoins(
        [1, 37, 19, 38, 11, 42, 18, 33, 6, 37, 15, 48, 23, 12, 41, 18, 27, 32]
    )
    == 37
)
assert (
    Solution().minimumCoins(
        [38, 23, 27, 32, 47, 45, 48, 24, 39, 26, 37, 42, 24, 45, 27, 26, 15, 16, 26, 6]
    )
    == 132
)
assert Solution().minimumCoins([26, 18, 6, 12, 49, 7, 45, 45]) == 39
assert Solution().minimumCoins([1, 10, 1, 1]) == 2
assert Solution().minimumCoins([3, 1, 2]) == 4


#
# @lcpr case=start
# [3,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,10,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [26,18,6,12,49,7,45,45]\n
# @lcpr case=end

#

#
# @lc app=leetcode.cn id=2952 lang=python3
# @lcpr version=30204
#
# [2952] 需要添加的硬币的最小数量
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        x = 0
        ret = 0
        idx=0
        N=len(coins)
        while x<target:
            if idx<N and coins[idx]<=x+1:
                x+=coins[idx]
                idx+=1
            else:
                x=2*x+1
                ret+=1
        return ret


# @lc code=end
assert Solution().minimumAddedCoins(coins = [1,1,1], target = 20) == 3
assert Solution().minimumAddedCoins(coins=[1, 4, 10, 5, 7, 19], target=19) == 1
assert Solution().minimumAddedCoins(coins=[1, 4, 10], target=19) == 2


#
# @lcpr case=start
# [1,4,10]\n19\n
# @lcpr case=end

# @lcpr case=start
# [1,4,10,5,7,19]\n19\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n20\n
# @lcpr case=end

#

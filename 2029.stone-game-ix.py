#
# @lc app=leetcode.cn id=2029 lang=python3
# @lcpr version=30204
#
# [2029] 石子游戏 IX
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:

        cnt = [0] * 3
        for s in stones:
            cnt[s % 3] += 1

        mx=max(cnt[1],cnt[2])
        mi=min(cnt[1],cnt[2])
        if cnt[0]&1:
            return mx-2>mi
        else:
            return mi>0

# @lc code=end
assert Solution().stoneGameIX([20, 3, 20, 17, 2, 12, 15, 17, 4]) == True
assert Solution().stoneGameIX([19,2,17,20,7,17]) == True
assert Solution().stoneGameIX([3, 3]) == False
assert Solution().stoneGameIX([5, 1, 2, 4, 3]) == False


#
# @lcpr case=start
# [2,1]\n
# @lcpr case=end

# @lcpr case=start
# [2]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,2,4,3]\n
# @lcpr case=end

#

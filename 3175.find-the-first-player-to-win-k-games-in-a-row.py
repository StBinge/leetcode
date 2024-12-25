#
# @lc app=leetcode.cn id=3175 lang=python3
# @lcpr version=30204
#
# [3175] 找到连续赢 K 场比赛的第一位玩家
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        N = len(skills)
        if k >= N:
            mx = 0
            for i, v in enumerate(skills):
                if v > skills[mx]:
                    mx = i
            return mx

        cnt = 0
        cur = 0
        mx = 0
        for i in range(1, N):
            sk = skills[i]
            if skills[cur] > sk:
                cnt += 1
            else:
                cnt = 1
                cur = i
            if cnt == k:
                return cur
        return cur


# @lc code=end
assert Solution().findWinningPlayer([4, 18, 17, 20, 15, 12, 8, 5], 1) == 1
assert Solution().findWinningPlayer(skills=[4, 2, 6, 3, 9], k=2) == 2
assert Solution().findWinningPlayer(skills=[2, 5, 4], k=3) == 1


#
# @lcpr case=start
# [4,2,6,3,9]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,5,4]\n3\n
# @lcpr case=end

#

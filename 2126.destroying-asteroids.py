#
# @lc app=leetcode.cn id=2126 lang=python3
# @lcpr version=30204
#
# [2126] 摧毁小行星
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        nxt=[]
        while len(asteroids)!=0:
            nxt.clear()
            for a in asteroids:
                if a<=mass:
                    mass+=a
                else:
                    nxt.append(a)
            if len(asteroids)==len(nxt):
                return False
            asteroids,nxt=nxt,asteroids
        return True
# @lc code=end
assert Solution().asteroidsDestroyed(86,[156,197,192,14,97,160,14,5])


#
# @lcpr case=start
# 10\n[3,9,19,5,21]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[4,9,23,4]\n
# @lcpr case=end

#


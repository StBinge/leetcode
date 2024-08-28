#
# @lc app=leetcode.cn id=2305 lang=python3
# @lcpr version=30204
#
# [2305] 公平分发饼干
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        m = 1 << len(cookies)
        SUM = [0] * m
        for i, v in enumerate(cookies):
            bit = 1 << i
            for j in range(bit):
                SUM[bit | j] = SUM[j] + v

        f=SUM.copy()
        for _ in range(1,k):
            for mask in range(m-1,0,-1):
                s=mask
                while s:
                    v=max(f[mask^s],SUM[s])
                    f[mask]=min(f[mask],v)
                    s=(s-1)&mask
        return f[-1]


# @lc code=end
assert Solution().distributeCookies([64,32,16,8,4,2,1,1000],8) == 1000
assert Solution().distributeCookies(cookies=[6, 1, 3, 2, 2, 4, 1, 2], k=3) == 7
assert Solution().distributeCookies(cookies=[8, 15, 10, 20, 8], k=2) == 31


#
# @lcpr case=start
# [8,15,10,20,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [6,1,3,2,2,4,1,2]\n3\n
# @lcpr case=end

#

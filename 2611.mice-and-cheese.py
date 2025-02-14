#
# @lc app=leetcode.cn id=2611 lang=python3
# @lcpr version=30204
#
# [2611] 老鼠和奶酪
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        N=len(reward1)
        sorted_idx=sorted(range(N),key=lambda x:reward1[x]-reward2[x],reverse=True)

        return sum(reward1[i] for i in sorted_idx[:k])+sum(reward2[i] for i in sorted_idx[k:])
# @lc code=end
assert Solution().miceAndCheese(reward1 = [1,1], reward2 = [1,1], k = 2)==2
assert Solution().miceAndCheese(reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2)==15


#
# @lcpr case=start
# [1,1,3,4]\n[4,4,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n[1,1]\n2\n
# @lcpr case=end

#


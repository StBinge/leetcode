#
# @lc app=leetcode.cn id=3413 lang=python3
# @lcpr version=30204
#
# [3413] 收集连续 K 个袋子可以获得的最多硬币数量
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        left_idx=coins[0][0]
        left_cid=0
        ret=0
        cur=0
        cur_len=0
        for right_cid,[l,r,c] in enumerate(coins):
            if r-left_idx+1<=k:
                cur+=(r-l+1)*c
                cur_len+=(r-l)
                continue
            dif=k-cur_len
            cur+=dif*c
            pl,pr,pc=coins[left_cid]
            if coins[left_cid][2]<c:
                move=min(pr-left_idx+1,)


# @lc code=end
assert Solution().maximumCoins([[1,1000000000,1000]],1000000000)==1000000000000
assert Solution().maximumCoins(coins = [[1,10,3]], k = 2)==6
assert Solution().maximumCoins(coins=[[8, 10, 1], [1, 3, 2], [5, 6, 4]], k=4)==10


#
# @lcpr case=start
# [[8,10,1],[1,3,2],[5,6,4]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[1,10,3]]\n2\n
# @lcpr case=end

#

#
# @lc app=leetcode.cn id=2379 lang=python3
# @lcpr version=30204
#
# [2379] 得到 K 个黑块的最少涂色次数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnt=blocks[:k].count('B')
        mx=cnt
        for i in range(k,len(blocks)):
            if blocks[i-k]=='B':
                cnt-=1
            if blocks[i]=='B':
                cnt+=1
            mx=max(mx,cnt)
            if mx==k:
                return 0
        return k-mx
# @lc code=end



#
# @lcpr case=start
# "WBBWWBBWBW"\n7\n
# @lcpr case=end

# @lcpr case=start
# "WBWBBBW"\n2\n
# @lcpr case=end

#


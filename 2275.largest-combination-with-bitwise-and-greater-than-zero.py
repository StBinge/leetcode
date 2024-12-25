#
# @lc app=leetcode.cn id=2275 lang=python3
# @lcpr version=30204
#
# [2275] 按位与结果大于零的最长组合
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        mx=max(candidates)
        mx_bits=len(str(bin(mx)))-2
        cnt=[0]*mx_bits
        for n in candidates:
            for i in range(mx_bits):
                if n&(1<<i):
                    cnt[i]+=1
        return max(cnt)
# @lc code=end



#
# @lcpr case=start
# [16,17,71,62,12,24,14]\n
# @lcpr case=end

# @lcpr case=start
# [8,8]\n
# @lcpr case=end

#


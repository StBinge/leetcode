#
# @lc app=leetcode.cn id=2014 lang=python3
# @lcpr version=30204
#
# [2014] 重复 K 次的最长子序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        MaxL=len(s)//2
        orda=ord('a')
        left,right=1,MaxL
        while left<right:
            mid=(left+right)>>1
            h=0
            for i in range(mid):
                h
# @lc code=end



#
# @lcpr case=start
# "letsleetcode"\n2\n
# @lcpr case=end

# @lcpr case=start
# "bb"\n2\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n2\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=3146 lang=python3
# @lcpr version=30204
#
# [3146] 两个字符串的排列差
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos={ch:i for i,ch in enumerate(s)}
        return sum(abs(i-pos[ch]) for i,ch in enumerate(t))

# @lc code=end



#
# @lcpr case=start
# "abc"\n"bac"\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n"edbac"\n
# @lcpr case=end

#


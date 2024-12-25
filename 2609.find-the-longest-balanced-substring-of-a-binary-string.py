#
# @lc app=leetcode.cn id=2609 lang=python3
# @lcpr version=30204
#
# [2609] 最长平衡子字符串
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        idx = 0
        N = len(s)
        ret = 0
        while idx < N:
            zero = 0
            while idx < N and s[idx] == "0":
                zero += 1
                idx += 1
            one = 0
            while idx < N and s[idx] == "1":
                one += 1
                idx += 1
            ret = max(ret, min(zero, one) * 2)
        return ret


# @lc code=end


#
# @lcpr case=start
# "01000111"\n
# @lcpr case=end

# @lcpr case=start
# "00111"\n
# @lcpr case=end

# @lcpr case=start
# "111"\n
# @lcpr case=end

#

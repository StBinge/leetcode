#
# @lc app=leetcode.cn id=2744 lang=python3
# @lcpr version=30204
#
# [2744] 最大字符串配对数目
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set()
        ret = 0
        for word in words:
            if word[::-1] in s:
                ret += 1
            else:
                s.add(word)
        return ret


# @lc code=end


#
# @lcpr case=start
# ["cd","ac","dc","ca","zz"]\n
# @lcpr case=end

# @lcpr case=start
# ["ab","ba","cc"]\n
# @lcpr case=end

# @lcpr case=start
# ["aa","ab"]\n
# @lcpr case=end

#

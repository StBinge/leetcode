#
# @lc app=leetcode.cn id=2982 lang=python3
# @lcpr version=30204
#
# [2982] 找出出现至少三次的最长特殊子字符串 II
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumLength(self, s: str) -> int:
        pre = ""
        cnt = 0
        cnts = defaultdict(list)
        for ch in s:
            if ch == pre:
                cnt += 1
            else:
                cnts[pre].append(cnt)
                pre = ch
                cnt = 1
        cnts[pre].append(cnt)
        ret = 0
        for ls in cnts.values():
            ls.sort(reverse=True)
            ls.extend([0, 0])
            v1, v2, v3 = ls[:3]
            ret = max(ret, v1 - 2, v3, min(v1 - 1, v2))
        return ret if ret > 0 else -1


# @lc code=end
assert Solution().maximumLength("abcaba") == 1
assert Solution().maximumLength("abcdef") == -1
assert Solution().maximumLength("aaaa") == 2


#
# @lcpr case=start
# "aaaa"\n
# @lcpr case=end

# @lcpr case=start
# "abcdef"\n
# @lcpr case=end

# @lcpr case=start
# "abcaba"\n
# @lcpr case=end

#

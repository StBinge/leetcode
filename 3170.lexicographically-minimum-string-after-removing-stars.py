#
# @lc app=leetcode.cn id=3170 lang=python3
# @lcpr version=30204
#
# [3170] 删除星号以后字典序最小的字符串
#

# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def clearStars(self, s: str) -> str:
        ss=list(s)
        pos_map=[[] for _ in range(26)]
        mask=0
        for i,ch in enumerate(s):
            if s[i]=='*':
                lb=mask & (-mask)
                idx=lb.bit_length()-1
                ss[pos_map[idx].pop()]='*'
                if not pos_map[idx]:
                    mask^=1<<idx
            else:
                code=ord(ch)-97
                pos_map[code].append(i)
                mask|=1<<code
        return ''.join(c for c in ss if c!='*')

# @lc code=end
assert Solution().clearStars("abc")=='abc'
assert Solution().clearStars("aaba*")=='aab'


#
# @lcpr case=start
# "aaba*"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

#


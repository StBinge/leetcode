#
# @lc app=leetcode.cn id=2810 lang=python3
# @lcpr version=30204
#
# [2810] 故障键盘
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def finalString(self, s: str) -> str:
        q=deque(maxlen=len(s))
        append_end=True
        for ch in s:
            if ch=='i':
                append_end=not append_end
                continue
            if append_end:
                q.append(ch)
            else:
                q.appendleft(ch)
        if not append_end:
            q=reversed(q)
        return ''.join(q)
# @lc code=end
assert Solution().finalString('poiinter')=='ponter'
assert Solution().finalString('string')=='rtsng'


#
# @lcpr case=start
# "string"\n
# @lcpr case=end

# @lcpr case=start
# "poiinter"\n
# @lcpr case=end

#


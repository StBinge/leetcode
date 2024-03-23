#
# @lc app=leetcode.cn id=3039 lang=python3
#
# [3039] 进行操作使字符串为空
#
from sbw import *
# @lc code=start
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        last_pos={ch:i for i,ch in enumerate(s)}
        cnt=Counter(s)
        max_times=max(cnt.values())
        ids=sorted(last_pos[k] for k,v in cnt.items() if v==max_times)
        return ''.join(map(s.__getitem__,ids))
# @lc code=end
assert Solution().lastNonEmptyString('abcd')=='abcd'
assert Solution().lastNonEmptyString('aabcbbca')=='ba'

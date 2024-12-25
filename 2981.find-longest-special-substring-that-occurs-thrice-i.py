#
# @lc app=leetcode.cn id=2981 lang=python3
# @lcpr version=30204
#
# [2981] 找出出现至少三次的最长特殊子字符串 I
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumLength(self, s: str) -> int:
        cnts=defaultdict(list)
        pre=s[0]
        left=0
        for i,ch in enumerate(s):
            if ch!=pre:
                cnts[pre].append(i-left)
                pre=ch
                left=i
        cnts[pre].append(len(s)-left)
        ret=-1
        for cnt in cnts.values():
            if max(cnt)<=ret:
                continue
            cnt.extend([-1,-1])
            cnt.sort(reverse=True)
            cur=max(cnt[2],cnt[0]-2,min(cnt[0]-1,cnt[1]))
            ret=max(ret,cur)
        return ret if ret else -1
# @lc code=end
assert Solution().maximumLength('acc')==-1
assert Solution().maximumLength('abcaba')==1
assert Solution().maximumLength('abcdef')==-1
assert Solution().maximumLength('aaaa')==2


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


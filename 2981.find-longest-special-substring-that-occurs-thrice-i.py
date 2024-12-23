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
        counter=defaultdict(list)
        pre=s[0]
        cnt=0
        for ch in s:
            if ch==pre:
                cnt+=1
            else:
                counter[pre].append(cnt)
                pre=ch
                cnt=1
        counter[pre].append(cnt)
        ret=0
        for ar in counter.values():
            ar.sort(reverse=True)
            ar.extend([0,0])
            ret=max(ret,ar[0]-2,min(ar[1],ar[0]-1),ar[2])
        return ret if ret>0 else -1
# @lc code=end
assert Solution().maximumLength('ceeeeeeeeeeeebmmmfffeeeeeeeeeeeewww')==11
assert Solution().maximumLength('abcccccdddd')==3
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


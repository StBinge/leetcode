#
# @lc app=leetcode.cn id=3324 lang=python3
# @lcpr version=30204
#
# [3324] 出现在屏幕上的字符串序列
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ret=[]
        for i,ch in enumerate(target):
            for j in range(97,ord(ch)+1):
                ret.append(target[:i]+chr(j))
        return ret
# @lc code=end
assert Solution().stringSequence('he')==["a","b","c","d","e","f","g","h","ha","hb","hc","hd","he"]
assert Solution().stringSequence('abc')==["a","aa","ab","aba","abb","abc"]


#
# @lcpr case=start
# "abc"\n
# @lcpr case=end

# @lcpr case=start
# "he"\n
# @lcpr case=end

#


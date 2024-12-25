#
# @lc app=leetcode.cn id=2788 lang=python3
# @lcpr version=30204
#
# [2788] 按分隔符拆分字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ret=[]
        for word in words:
            start=0
            for i,ch in enumerate(word):
                if ch==separator:
                    part=word[start:i]
                    if part:
                        ret.append(part)
                    start=i+1
            part=word[start:]
            if part:
                ret.append(part)
        return ret
# @lc code=end
assert Solution().splitWordsBySeparator(["$easy$","$problem$"],'$')==["easy","problem"]


#
# @lcpr case=start
# ["one.two.three","four.five","six"]\n"."\n
# @lcpr case=end

# @lcpr case=start
# ["$easy$","$problem$"]\n"$"\n
# @lcpr case=end

# @lcpr case=start
# ["|||"]\n"|"\n
# @lcpr case=end

#


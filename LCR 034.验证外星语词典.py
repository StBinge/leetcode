#
# @lc app=leetcode.cn id=LCR 034 lang=python3
# @lcpr version=30204
#
# [LCR 034] 验证外星语词典
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map={ch:i for i,ch in enumerate(order)}
        for x,y in pairwise(words):
            for c1,c2 in zip(x,y):
                if order_map[c1]>order_map[c2]:
                    return False
                elif order_map[c1]<order_map[c2]:
                    break
            else:
                if len(x)>len(y):
                    return False
        return True

# @lc code=end



#
# @lcpr case=start
# ["hello","leetcode"]\n"hlabcdefgijkmnopqrstuvwxyz"\n
# @lcpr case=end

# @lcpr case=start
# ["word","world","row"]\n"worldabcefghijkmnpqstuvxyz"\n
# @lcpr case=end

# @lcpr case=start
# ["apple","app"]\n"abcdefghijklmnopqrstuvwxyz"\n
# @lcpr case=end

#


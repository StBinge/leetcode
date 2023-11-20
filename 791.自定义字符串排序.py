#
# @lc app=leetcode.cn id=791 lang=python3
#
# [791] 自定义字符串排序
#

# @lc code=start
from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter=Counter(s)
        ret=[]
        for c in order:
            ret.append(c*counter[c])
            counter[c]=0
        for k,v in counter.items():
            if v>0:
                ret.append(k*v)
        return ''.join(ret)
# @lc code=end
order = "cba"
s = "abcd"
print(Solution().customSortString(order,s))
order = "cbafg"
s = "abcd"
print(Solution().customSortString(order,s))

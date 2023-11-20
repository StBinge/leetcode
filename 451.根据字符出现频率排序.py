#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter=Counter(s)
        frequency=[[k,v] for k,v in counter.items()]
        frequency.sort(key=lambda x:x[1],reverse=True)
        ret=[]
        for k,v in frequency:
            ret.append(k*v)
        return ''.join(ret)
# @lc code=end
assert Solution().frequencySort('tree')=='eert'
assert Solution().frequencySort('cccaaa')=='cccaaa'
assert Solution().frequencySort('Aabb')=='bbAa'

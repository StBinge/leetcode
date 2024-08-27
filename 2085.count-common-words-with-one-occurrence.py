#
# @lc app=leetcode.cn id=2085 lang=python3
# @lcpr version=30204
#
# [2085] 统计出现过一次的公共字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1=Counter(words1)
        cnt2=Counter(words2)
        ret=0
        for k1 in cnt1.keys():
            if cnt1[k1]==1 and cnt2[k1]==1:
                ret+=1
        return ret

# @lc code=end

assert Solution().countWords()

#
# @lcpr case=start
# ["leetcode","is","amazing","as","is"]\n["amazing","leetcode","is"]\n
# @lcpr case=end

# @lcpr case=start
# ["b","bb","bbb"]\n["a","aa","aaa"]\n
# @lcpr case=end

# @lcpr case=start
# ["a","ab"]\n["a","a","a","ab"]\n
# @lcpr case=end

#


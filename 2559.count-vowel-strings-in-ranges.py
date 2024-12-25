#
# @lc app=leetcode.cn id=2559 lang=python3
# @lcpr version=30204
#
# [2559] 统计范围内的元音字符串数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        presum=[0]
        vows='aeiou'
        for word in words:
            presum.append(presum[-1]+(word[0] in vows and word[-1] in vows))
        ret=[]
        for l,r in queries:
            ret.append(presum[r+1]-presum[l])
        return ret
# @lc code=end



#
# @lcpr case=start
# ["aba","bcb","ece","aa","e"]\n[[0,2],[1,4],[1,1]]\n
# @lcpr case=end

# @lcpr case=start
# ["a","e","i"]\n[[0,2],[0,1],[2,2]]\n
# @lcpr case=end

#


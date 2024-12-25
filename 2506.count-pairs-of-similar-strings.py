#
# @lc app=leetcode.cn id=2506 lang=python3
# @lcpr version=30204
#
# [2506] 统计相似字符串对的数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        cnt=defaultdict(int)
        ret=0
        for word in words:
            mask=0
            for ch in word:
                mask|=1<<(ord(ch)-ord('a'))
            ret+=cnt[mask]
            cnt[mask]+=1
        return ret
# @lc code=end



#
# @lcpr case=start
# ["aba","aabb","abcd","bac","aabc"]\n
# @lcpr case=end

# @lcpr case=start
# ["aabb","ab","ba"]\n
# @lcpr case=end

# @lcpr case=start
# ["nba","cba","dba"]\n
# @lcpr case=end

#


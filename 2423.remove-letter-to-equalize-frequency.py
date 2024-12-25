#
# @lc app=leetcode.cn id=2423 lang=python3
# @lcpr version=30204
#
# [2423] 删除字符使频率相同
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt=Counter(word)
        if len(cnt)==1 or len(cnt)==len(word):
            return True
        cnt_cnt=Counter(cnt.values())
        if len(cnt_cnt)!=2:
            return False
        if cnt_cnt[1]==1:
            return True
        k1,k2=list(cnt_cnt.keys())
        if k1>k2:
            k1,k2=k2,k1
        return k1+1==k2 and cnt_cnt[k2]==1
# @lc code=end



#
# @lcpr case=start
# "abcc"\n
# @lcpr case=end

# @lcpr case=start
# "aazz"\n
# @lcpr case=end

#


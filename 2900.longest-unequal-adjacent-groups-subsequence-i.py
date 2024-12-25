#
# @lc app=leetcode.cn id=2900 lang=python3
# @lcpr version=30204
#
# [2900] 最长相邻不相等子序列 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def dfs(pre):
            ret=[]
            for g,word in zip(groups,words):
                if g!=pre:
                    ret.append(word)
                    pre=g
            return ret
        
        ret1=dfs(0)
        ret2=dfs(1)
        return ret1 if len(ret1)>len(ret2) else ret2

# @lc code=end



#
# @lcpr case=start
# ["e","a","b"]\n[0,0,1]\n
# @lcpr case=end

# @lcpr case=start
# ["a","b","c","d"]\n[1,0,1,1]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=2707 lang=python3
# @lcpr version=30204
#
# [2707] 字符串中的额外字符
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N=len(s)
        pos_map=[[] for _ in range(N)]
        for word in dictionary:
            idx=0
            m=len(word)
            while True:
                idx=s.find(word,idx)
                if idx==-1:
                    break
                pos_map[idx].append(len(word))
                idx+=m
        f=[float('inf')]*(N+1)
        f[-1]=0
        for i in range(N-1,-1,-1):
            f[i]=f[i+1]+1
            for jump in pos_map[i]:
                f[i]=min(f[i],f[i+jump])
        return f[0]
# @lc code=end
assert Solution().minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"])==3
assert Solution().minExtraChar("leetscode",["leet","code","leetcode"])==1


#
# @lcpr case=start
# "leetscode"\n["leet","code","leetcode"]\n
# @lcpr case=end

# @lcpr case=start
# "sayhelloworld"\n["hello","world"]\n
# @lcpr case=end

#


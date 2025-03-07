#
# @lc app=leetcode.cn id=3331 lang=python3
# @lcpr version=30204
#
# [3331] 修改后子树的大小
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        N=len(parent)
        g=[[] for _ in range(N)]
        for i in range(1,N):
            g[parent[i]].append(i)
        char_pos=[-1]*26
        size=[1]*N
        def dfs(x):
            code=ord(s[x])-97
            last_pos=char_pos[code]
            char_pos[code]=x
            for nxt in g[x]:
                dfs(nxt)
                _code=ord(s[nxt])-97
                anc=char_pos[_code]
                size[x if anc<0 else anc]+=size[nxt]
            char_pos[code]=last_pos
        dfs(0)
        return size

# @lc code=end
assert Solution().findSubtreeSizes(parent = [-1,0,4,0,1], s = "abbba")==[5,2,1,1,1]
assert Solution().findSubtreeSizes(parent = [-1,0,0,1,1,1], s = "abaabc")==[6,3,1,1,1,1]


#
# @lcpr case=start
# [-1,0,0,1,1,1]\n"abaabc"\n
# @lcpr case=end

# @lcpr case=start
# [-1,0,4,0,1]\n"abbba"\n
# @lcpr case=end

#


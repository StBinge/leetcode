#
# @lc app=leetcode.cn id=1593 lang=python3
#
# [1593] 拆分字符串使唯一子字符串的数目最大
#


# @lc code=start
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N=len(s)
        ss=set()
        def dfs(i):
            if i==N:
                return 0
            ret=0
            for j in range(i,N):
                if s[i:j+1] not in ss:
                    if ret>=len(ss)+N-j:
                        break
                    ss.add(s[i:j+1])
                    ret=max(ret,1+dfs(j+1))
                    ss.remove(s[i:j+1])
            return ret
        return dfs(0)


# @lc code=end
assert Solution().maxUniqueSplit("aa") == 1
assert Solution().maxUniqueSplit("aba") == 2
assert Solution().maxUniqueSplit("ababccc") == 5

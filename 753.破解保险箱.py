#
# @lc app=leetcode.cn id=753 lang=python3
#
# [753] 破解保险箱
#

# @lc code=start
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        seen = set()
        ans = list()
        highest = 10 ** (n - 1)

        def dfs(node: int):
            for x in range(k):
                nei = node * 10 + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei % highest)
                    ans.append(str(x))

        dfs(0)
        return "".join(ans) + "0" * (n - 1)


# @lc code=end

assert Solution().crackSafe(2,2)=='01100'
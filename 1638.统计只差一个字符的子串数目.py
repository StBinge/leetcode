#
# @lc app=leetcode.cn id=1638 lang=python3
#
# [1638] 统计只差一个字符的子串数目
#


# @lc code=start
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        N1, N2 = len(s), len(t)
        ret = 0
        for i in range(N1):
            for j in range(N2):
                dif=0
                offset=0
                while i+offset<N1 and j+offset<N2 and dif<1:
                    if s[i+offset]!=t[j+offset]:
                        dif+=1
                    offset+=1
                if dif==1:
                    ret+=1
                else:
                    continue
                while i+offset<N1 and j+offset<N2 and s[i+offset]==t[j+offset]:
                    ret+=1
                    offset+=1
        return ret

# @lc code=end
assert Solution().countSubstrings(s="abe", t="bbc") == 10
assert Solution().countSubstrings(s="a", t="a") == 0
assert Solution().countSubstrings(s="ab", t="bb") == 3
assert Solution().countSubstrings(s="aba", t="baba") == 6

#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        ret=0
        for i in range(len(s)):
            if (i==0 or s[i-1]==' ') and s[i]!=' ':
                ret+=1
        return ret

# @lc code=end
assert Solution().countSegments("love live! mu'sic forever")==4
assert Solution().countSegments("Hello, my name is John")==5

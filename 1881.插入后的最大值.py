#
# @lc app=leetcode.cn id=1881 lang=python3
#
# [1881] 插入后的最大值
#

# @lc code=start
class Solution:
    def maxValue(self, n: str, x: int) -> str:

        if n[0]=='-':
            for i in range(1,len(n)):
                if int(n[i])>x:
                    return n[:i]+str(x)+n[i:]
        else:
            for i in range(len(n)):
                if int(n[i])<x:
                    return n[:i]+str(x)+n[i:]
        return n+str(x)
# @lc code=end
assert Solution().maxValue('-13',2)=='-123'
assert Solution().maxValue('99',9)=='999'

#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉 K 位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        L=len(num)
        cnt=L-k
        if cnt==0:
            return '0'
        stack=[]
        for n in num:
            while k and stack and stack[-1]>n:
                stack.pop()
                k-=1
            stack.append(n)
        return ''.join(stack[:len(stack)-k]).lstrip('0') or '0'
       
        
# @lc code=end

assert Solution().removeKdigits('1432219',3)=='1219'
assert Solution().removeKdigits('10200',1)=='200'
assert Solution().removeKdigits('10',2)=='0'
assert Solution().removeKdigits('10',1)=='0'
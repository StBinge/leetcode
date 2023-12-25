#
# @lc app=leetcode.cn id=1006 lang=python3
#
# [1006] 笨阶乘
#

# @lc code=start
class Solution:
    def clumsy(self, n: int) -> int:
        stack=[n]
        op=0
        for i in range(n-1,0,-1):
            op%=4
            if op==0:
                stack.append(stack.pop()*i)
            elif op==1:
                cur=stack.pop()
                flag=1 if cur>=0 else -1
                stack.append(flag * (abs(cur)//i))
            elif op==2:
                stack.append(i)
            else:
                stack.append(-i)
            op+=1
        return sum(stack)
# @lc code=end
assert Solution().clumsy(10)==12
assert Solution().clumsy(4)==7

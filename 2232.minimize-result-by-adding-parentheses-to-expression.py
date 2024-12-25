#
# @lc app=leetcode.cn id=2232 lang=python3
# @lcpr version=30204
#
# [2232] 向表达式添加括号后的最小结果
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimizeResult(self, expression: str) -> str:
        left,right=expression.split('+')
        mi=int(left)+int(right)
        ret='('+expression+')'
        for i in range(len(left)):
            l_mul=1 if i==0 else int(left[:i])
            l_add=int(left[i:])
            for j in range(len(right)):
                r_add=int(right[:j+1])
                r_mul=1 if j==len(right)-1 else int(right[j+1:])
                val=(l_add+r_add)*l_mul*r_mul
                if val<mi:
                    mi=val
                    ret=f'{left[:i]}({left[i:]}+{right[:j+1]}){right[j+1:]}'
        return ret
# @lc code=end



#
# @lcpr case=start
# "247+38"\n
# @lcpr case=end

# @lcpr case=start
# "12+34"\n
# @lcpr case=end

# @lcpr case=start
# "999+999"\n
# @lcpr case=end

#


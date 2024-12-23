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
        # left=int(left)
        # right=int(right)
        val=int(left)+int(right)
        ret='('+expression+')'
        for i in range(len(left)):
            p1=1 if i==0 else int(left[:i])
            add1=int(left[i:])
            for j in range(len(right)):
                add2=int(right[:j+1])
                p2=1 if j+1==len(right) else int(right[j+1:])
                v=p1*p2*(add1+add2)
                if v<val:
                    ret=f'{left[:i]}({left[i:]}+{right[:j+1]}){right[j+1:]}'
                    val=v
        return ret
# @lc code=end
assert Solution().minimizeResult("999+999")=="(999+999)"
assert Solution().minimizeResult("12+34")=="1(2+3)4"
assert Solution().minimizeResult('247+38')=="2(47+38)"


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


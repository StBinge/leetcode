#
# @lc app=leetcode.cn id=1896 lang=python3
#
# [1896] 反转表达式值的最少操作次数
#
from sbw import *


# @lc code=start
class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        N=len(expression)
        def eval(idx):
            start=idx
            vals = []
            op = []
            while idx <N:
                ch = expression[idx]
                if ch == "(":
                    val,idx=eval(idx+1)
                    vals.append(val)
                elif ch==')':
                    break
                if ch == "1":
                    vals.append([1, 0])
                elif ch == "0":
                    vals.append([0, 1])
                elif ch in "&|":
                    op.append(ch)
                idx += 1

            c0, c1 = vals[0]
            op_cnt = len(op)
            for i in range(op_cnt):
                nxt0, nxt1 = vals[i + 1]
                if op[i] == "&":
                    _c0 = min(
                        # x&y=0
                        c0 + nxt1,
                        c1 + nxt0,
                        c0 + nxt0,
                        # change to x|y=0
                        1 + c0 + nxt0,
                    )
                    _c1 = min(
                        # x&y=1
                        c1 + nxt1,
                        # change to x|y=1
                        1 + min(c1 + nxt0, c1 + nxt1, c0 + nxt1),
                    )
                else:
                    _c0 = min(
                        # x|y=0
                        c0 + nxt0,
                        # change to x&y=0
                        1 + min(c0 + nxt0, c0 + nxt1, c1 + nxt0),
                    )
                    _c1 = min(
                        # x|y=1
                        c0 + nxt1,
                        c1 + nxt0,
                        c1 + nxt1,
                        # change to x&y=1
                        1 + c1 + nxt1,
                    )
                c0,c1=_c0,_c1
            return [c0, c1],idx

        [c0, c1],_ = eval(0)
        return c0 | c1


# @lc code=end

assert Solution().minOperationsToFlip("0|0|1&0|(1|0&0&(0&0))") == 1
assert Solution().minOperationsToFlip("(((0)&1&((0&0))))") == 2
assert Solution().minOperationsToFlip("(0&0)&(0&0&0)") == 3
assert Solution().minOperationsToFlip("(0|(1|0&1))") == 1
assert Solution().minOperationsToFlip("1&(0|1)") == 1

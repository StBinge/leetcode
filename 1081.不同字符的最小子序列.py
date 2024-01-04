#
# @lc app=leetcode.cn id=1081 lang=python3
#
# [1081] 不同字符的最小子序列
#
from sbw import *
# @lc code=start
import bisect
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        chars=Counter(s)
        stack=[]
        include=set()
        for c in s:
            chars[c]-=1
            # if include[c]
            if c in include:
                continue
            # if chars[c]==0:
            #     stack.append(c)
            #     include.add(c)
            #     continue
            while stack:
                pre=stack[-1]
                if pre>c and chars[pre]>0:
                    stack.pop()
                    include.discard(pre)
                else:
                    break

            stack.append(c)
            include.add(c)

        return ''.join(stack)
# @lc code=end
assert Solution().smallestSubsequence('pblspykdpqfhcfcirkrhbbfbnqagshfqrrkcjpsuaytjfwyhjpubttxkkpswuvoiicsnkxiyhsyqrqecsiabhvjfodpkdgcgdceobyfonnurqxvstxkgsagnosvfjgsnylyhbjcrkgaylgxxxmghfbpfqwpplntrrogtkapbpkkwkdxgrfmikdlcftuyywrsnfasxgiw')=='abcdefgnosvhjklmpqituyrxw'
assert Solution().smallestSubsequence('cbacdcbc')=='acdb'
assert Solution().smallestSubsequence('bcabc')=='abc'

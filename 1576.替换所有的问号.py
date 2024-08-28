#
# @lc app=leetcode.cn id=1576 lang=python3
#
# [1576] 替换所有的问号
#

from sbw import *
# @lc code=start
class Solution:
    def modifyString(self, s: str) -> str:
        ret=[]
        n=len(s)
        for i,ch in enumerate(s):
            if ch!="?":
                ret.append(ch)
                continue
            for cur in 'abc':
                pre=ret[-1] if ret else ''
                nxt=s[i+1] if i+1<n else ''
                if cur!=pre and cur!=nxt:
                    ret.append(cur)
                    break
        return "".join(ret)


# @lc code=end
assert all(x!=y for x,y in pairwise(Solution().modifyString("??yw?ipkj?")))
assert all(x!=y for x,y in pairwise(Solution().modifyString("?zs")))
assert all(x!=y for x,y in pairwise(Solution().modifyString("ubv?w")))

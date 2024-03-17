#
# @lc app=leetcode.cn id=1370 lang=python3
#
# [1370] 上升下降字符串
#
from sbw import *
# @lc code=start
class Solution:
    def sortString(self, s: str) -> str:
        orda=ord('a')
        q=deque([[chr(i+orda),0] for i in range(26)])
        for c in s:
            q[ord(c)-orda][1]+=1
        ret=''
        while q:
            for i in range(len(q)):
                if q[i][1]:
                    ret+=q[i][0]
                    q[i][1]-=1
            for i in range(len(q)-1,-1,-1):
                if q[i][1]:
                    ret+=q[i][0]
                    q[i][1]-=1
            while q and q[0][1]==0:
                q.popleft()
            while q and q[-1][1]==0:
                q.pop()
            if len(q)==1:
                ret+=q[0][0]*q[0][1]
                return ret
        return ret
# @lc code=end
assert Solution().sortString('ggggggg')=='ggggggg'
assert Solution().sortString('leetcode')=='cdelotee'
assert Solution().sortString('rat')=='art'
assert Solution().sortString('aaaabbbbcccc')=='abccbaabccba'

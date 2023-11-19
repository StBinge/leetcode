#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
from collections import deque
class Solution:
    def firstUniqChar(self, s: str) -> int:
        stack=[]
        cnt=[0]*26
        for i in range(len(s)-1,-1,-1):
            id=ord(s[i])-ord('a')
            cnt[id]+=1
            if cnt[id]==1:
                stack.append([id,i])
            else:
                while stack and cnt[stack[-1][0]]>1:
                    stack.pop()
        return stack[-1][1] if stack else -1
# @lc code=end
assert Solution().firstUniqChar('loveleetcode')==2
assert Solution().firstUniqChar('leetcode')==0
assert Solution().firstUniqChar('aabb')==-1

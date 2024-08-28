#
# @lc app=leetcode.cn id=1647 lang=python3
#
# [1647] 字符频次唯一的最小删除次数
#
from sbw import *
# @lc code=start
class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = [0]*26
        for c in s:
            cnt[ord(c)-ord('a')] += 1
        cnt.sort(reverse=True)
        while cnt and cnt[-1]==0:
            cnt.pop()
        ret=0
        nxt=float('inf')
        for i in range(len(cnt)):
            if cnt[i]<=nxt:
                nxt=cnt[i]-1
                continue
            else:
                ret+=cnt[i]-nxt
                nxt=max(0,nxt-1)
        return ret

# @lc code=end
assert Solution().minDeletions('bbcebab')==2
assert Solution().minDeletions('ceabaacb')==2
assert Solution().minDeletions('aaabbbcc')==2
assert Solution().minDeletions('aab')==0

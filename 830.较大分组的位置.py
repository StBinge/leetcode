#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#
from typing import List
# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ret=[]
        n=len(s)
        cnt=1
        for i in range(n):
            if i==n-1 or s[i]!=s[i+1]:
                if cnt>2:
                    ret.append([i-cnt+1,i])
                cnt=1
            else:
                cnt+=1
        return ret
# @lc code=end
s = "abcdddeeeeaabbbcd"
ret=[[3,5],[6,9],[12,14]]
assert Solution().largeGroupPositions(s)==ret

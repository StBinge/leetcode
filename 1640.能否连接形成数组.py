#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#
from sbw import *
# @lc code=start
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pos={}
        for i,p in enumerate(pieces):
            pos[p[0]]=i
        
        piece=[]
        pid=0
        for i in range(len(arr)):
            if pid==len(piece):
                if arr[i] not in pos:
                    return False
                piece=pieces[pos[arr[i]]]
                pid=0
            if arr[i]!=piece[pid]:
                return False
            pid+=1
        return True
# @lc code=end
assert Solution().canFormArray(arr = [49,18,16], pieces = [[16,18,49]])==False
assert Solution().canFormArray(arr = [15,88], pieces = [[88],[15]])

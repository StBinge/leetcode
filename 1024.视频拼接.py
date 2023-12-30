#
# @lc app=leetcode.cn id=1024 lang=python3
#
# [1024] 视频拼接
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        maxn=[0]*time
        for a,b in clips:
            if a<time:
                maxn[a]=max(maxn[a],b)
        ret=0
        last=pre=0
        for t in range(time):
            last=max(last,maxn[t])
            if last==t:
                return -1
            if t==pre:
                ret+=1
                pre=last
        return ret
 

                
# @lc code=end
clips=[[3,12],[7,14],[9,14],[12,15],[0,9],[4,14],[2,7],[1,11]]
time=10
assert Solution().videoStitching(clips,time)==2

clips=[[8,10],[17,39],[18,19],[8,16],[13,35],[33,39],[11,19],[18,35]]
time=20
assert Solution().videoStitching(clips,time)==-1

clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
time = 9
assert Solution().videoStitching(clips,time)==3

clips = [[0,1],[1,2]]
time = 5
assert Solution().videoStitching(clips,time)==-1
clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
time = 10
assert Solution().videoStitching(clips,time)==3

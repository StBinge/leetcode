#
# @lc app=leetcode.cn id=1345 lang=python3
#
# [1345] 跳跃游戏 IV
#
from sbw import *
# @lc code=start
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        L=len(arr)
        if L==1:
            return 0
        pos_map={}
        for i,n in enumerate(arr):
            pos_map.setdefault(n,[]).append(i)
        q=deque([0])
        vis=[False]*L
        vis[0]=True
        step=0
        while q:
            step+=1
            for i in range(len(q)):
                cur=q.popleft()
                pre=cur-1
                if pre==L-1:
                    return step
                if pre>=0 and vis[pre]==False:
                    q.append(pre)
                    vis[pre]=True
                nxt=cur+1
                if nxt==L-1:
                    return step
                if nxt<L and vis[nxt]==False:
                    q.append(nxt)
                    vis[nxt]==True
                for pos in pos_map[arr[cur]]:
                    if pos==L-1:
                        return step
                    if vis[pos]==False:
                        q.append(pos)
                        vis[pos]=True
                pos_map[arr[cur]]=[]
            
# @lc code=end
assert Solution().minJumps([7,6,9,6,9,6,9,7])==1
assert Solution().minJumps([7])==0
assert Solution().minJumps([100,-23,-23,404,100,23,23,23,3,404])==3

#
# @lc app=leetcode.cn id=1311 lang=python3
#
# [1311] 获取你好友已观看的视频
#
from sbw import *
# @lc code=start
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        N=len(friends)
        vis=[False]*N

        q=deque([id])
        vis[id]=True
        k=0
        while q:
            k+=1
            for i in range(len(q)):
                cur=q.popleft()
                for f in friends[cur]:
                    if not vis[f]:
                        q.append(f)
                        vis[f]=True
            if k==level:
                break
        ret=defaultdict(int)
        for p in q:
            for v in watchedVideos[p]:
                ret[v]+=1
        ret=sorted(ret.items(),key=lambda x:(x[1],x[0]))
        return [x[0] for x in ret]
# @lc code=end

assert Solution().watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2)==['D'] 
assert Solution().watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1)==["B","C"] 
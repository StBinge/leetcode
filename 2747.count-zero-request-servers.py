#
# @lc app=leetcode.cn id=2747 lang=python3
# @lcpr version=30204
#
# [2747] 统计没有收到请求的服务器数目
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x:x[1])
        sorted_qidx=sorted(range(len(queries)),key=queries.__getitem__)
        log_cnt=defaultdict(int)
        left=queries[sorted_qidx[0]]-x        
        left_id=0
        M=len(logs)
        while left_id<M and logs[left_id][1]<left:
            left_id+=1
        if left_id==M:
            return [n]*len(queries)
        right_id=left_id
        ret=[0]*len(queries)
        cur_cnt=0
        for qidx in sorted_qidx:
            left,right=queries[qidx]-x,queries[qidx]
            while right_id<M and logs[right_id][1]<=right:
                log_cnt[logs[right_id][0]]+=1
                if log_cnt[logs[right_id][0]]==1:
                    cur_cnt+=1
                right_id+=1
            
            while left_id<right_id and logs[left_id][1]<left:
                log_cnt[logs[left_id][0]]-=1
                if log_cnt[logs[left_id][0]]==0:
                    cur_cnt-=1
                left_id+=1
            ret[qidx]=n- cur_cnt
        return ret
# @lc code=end
assert Solution().countServers(5,[[3,4],[5,1],[4,6]],10,[32,29])==[5,5]
assert Solution().countServers(6,[[1,21]],10,[24,35,28,26,20,25,16,31,12])==[5,6,5,5,6,5,6,5,6]
assert Solution().countServers(n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4])==[0,1]
assert Solution().countServers(n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11])==[1,2]


#
# @lcpr case=start
# 3\n[[1,3],[2,6],[1,5]]\n5\n[10,11]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[2,4],[2,1],[1,2],[3,1]]\n2\n[3,4]\n
# @lcpr case=end

#


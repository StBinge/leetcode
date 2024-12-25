#
# @lc app=leetcode.cn id=2179 lang=python3
# @lcpr version=30204
#
# [2179] 统计数组中好三元组数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Seg:
    def __init__(self,n) -> None:
        self.n=n
        self.vals=[0]*(n+1)
    
    def add(self,x):
        while x<=self.n:
            self.vals[x]+=1
            x+=x&-x
    
    def query(self,x):
        ret=0
        while x>0:
            ret+=self.vals[x]
            x-=x&-x
        return ret
    
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        N=len(nums2)
        pos_map={n:i for i,n in enumerate(nums1)}
        # sorted_idx=sorted(range(N),key=lambda x:pos_map[nums2[x]])
        ret=0
        seg=Seg(N)
        for i,n in enumerate(nums2):
            idx=pos_map[n]
            less=seg.query(idx)
            big=N-1-idx-i+less
            ret+=less*big
            seg.add(idx+1)
        return ret


# @lc code=end
assert Solution().goodTriplets([13,14,10,2,12,3,9,11,15,8,4,7,0,6,5,1],[8,7,9,5,6,14,15,10,2,11,4,13,3,12,1,0])==77
assert Solution().goodTriplets(nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3])==4
assert Solution().goodTriplets(nums1 = [2,0,1,3], nums2 = [0,1,2,3])==1


#
# @lcpr case=start
# [2,0,1,3]\n[0,1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,0,1,3,2]\n[4,1,0,2,3]\n
# @lcpr case=end

#


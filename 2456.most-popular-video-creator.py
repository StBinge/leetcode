#
# @lc app=leetcode.cn id=2456 lang=python3
# @lcpr version=30204
#
# [2456] 最流行的视频创作者
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creator_score=defaultdict(int)
        creator_mxvid={}
        idx=0
        for creator,vid,view in zip(creators,ids,views):
            creator_score[creator]+=view
            if creator not in creator_mxvid or view>views[creator_mxvid[creator]] or (views[creator_mxvid[creator]]==view and vid<ids[creator_mxvid[creator]]):
                creator_mxvid[creator]=idx
            idx+=1
        ret=[]
        ret_creators=[]
        mx_score=0
        for cr,score in creator_score.items():
            if score>mx_score:
                mx_score=score
                ret_creators=[cr]
            elif score==mx_score:
                ret_creators.append(cr)
        
        for cr in ret_creators:
            ret.append([cr,ids[creator_mxvid[cr]]])
        return ret
# @lc code=end
assert Solution().mostPopularCreator(creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4])==[["alice","one"],["bob","two"]]


#
# @lcpr case=start
# ["alice","bob","alice","chris"]\n["one","two","three","four"]\n[5,10,5,4]\n
# @lcpr case=end

# @lcpr case=start
# ["alice","alice","alice"]\n["a","b","c"]\n[1,2,2]\n
# @lcpr case=end

#


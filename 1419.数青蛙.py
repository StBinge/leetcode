#
# @lc app=leetcode.cn id=1419 lang=python3
#
# [1419] 数青蛙
#

# @lc code=start
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ret=0
        # c=r=o=a=0
        ids={
            'c':0,
            'r':1,
            'o':2,
            'a':3,
            'k':4,
        }
        cnt=[0]*4
        for ch in croakOfFrogs:
            idx=ids[ch]
            if idx==0:
                cnt[0]+=1
                ret=max(ret,cnt[0])
            elif idx!=4:
                cnt[idx]+=1
                if cnt[idx]>cnt[idx-1]:
                    return -1
            else:
                if cnt[3]<1:
                    return -1
                cnt[0]-=1
                cnt[1]-=1
                cnt[2]-=1
                cnt[3]-=1
        return ret if cnt[0]==0 else -1
# @lc code=end
assert Solution().minNumberOfFrogs('crcoakroak')==2
assert Solution().minNumberOfFrogs('croakcroa')==-1
assert Solution().minNumberOfFrogs('croakcrook')==-1
assert Solution().minNumberOfFrogs('croakcroak')==1

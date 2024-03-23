#
# @lc app=leetcode.cn id=1405 lang=python3
#
# [1405] 最长快乐字符串
#

# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        cnt=[[a,'a'],[b,'b'],[c,'c']]
        ret=[]
        while True:
            cnt.sort(reverse=True)
            has_next=False
            for i,[c,ch] in enumerate(cnt):
                if c==0:
                    break
                if len(ret)>1 and ret[-1]==ch and ret[-2]==ch:
                    continue
                ret.append(ch)
                cnt[i][0]-=1
                has_next=True
                break
            if not has_next:
                return ''.join(ret)





        
# @lc code=end
assert  len(Solution().longestDiverseString(0,0,7))==2
assert  len(Solution().longestDiverseString(7,1,0))==5
assert  len(Solution().longestDiverseString(2,2,1))==5
assert  len(Solution().longestDiverseString(1,1,7))==8

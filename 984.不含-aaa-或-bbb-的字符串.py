#
# @lc app=leetcode.cn id=984 lang=python3
#
# [984] 不含 AAA 或 BBB 的字符串
#

# @lc code=start
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:

        chars='ab'
        cnt=[a,b]
        if b>a:
            chars='ba'
            cnt=[b,a]
        dif=cnt[0]-cnt[1]
        leader_cnt=min(cnt[1],dif)
        pair_cnt=cnt[1]-leader_cnt
        return (chars[0]*2+chars[1])*leader_cnt+(chars[0]+chars[1])*pair_cnt+chars[0]*(cnt[0]-leader_cnt*2-pair_cnt)
        
        
# @lc code=end
print(Solution().strWithout3a3b(4,1))
print(Solution().strWithout3a3b(1,2))

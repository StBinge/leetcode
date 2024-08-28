#
# @lc app=leetcode.cn id=1927 lang=python3
# @lcpr version=30204
#
# [1927] 求和游戏
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sumGame(self, num: str) -> bool:
        N=len(num)
        left_sum=right_sum=left_cnt=right_cnt=0
        for i in range(N//2):
            if num[i] =='?':
                left_cnt+=1
            else:
                left_sum+=int(num[i])
            if num[-1-i]=='?':
                right_cnt+=1
            else:
                right_sum+=int(num[-i-1])
        
        return (left_cnt+right_cnt)%2 or left_sum-right_sum!=(right_cnt-left_cnt)*9//2


# @lc code=end
assert Solution().sumGame('?3295???')==False
assert Solution().sumGame('5023')==False
assert Solution().sumGame('25??')


#
# @lcpr case=start
# "5023"\n
# @lcpr case=end

# @lcpr case=start
# "25??"\n
# @lcpr case=end

# @lcpr case=start
# "?3295???"\n
# @lcpr case=end

#


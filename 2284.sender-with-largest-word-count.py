#
# @lc app=leetcode.cn id=2284 lang=python3
# @lcpr version=30204
#
# [2284] 最多单词数的发件人
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        cnt=defaultdict(int)
        for mes,sender in zip(messages,senders):
            cnt[sender]+=mes.count(' ')+1
        mx=0
        ret=''
        for k,v in cnt.items():
            if v>mx:
                ret=k
                mx=v
            elif v==mx:
                ret=max(ret,k)
        return ret
# @lc code=end



#
# @lcpr case=start
# ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"]\n["Alice","userTwo","userThree","Alice"]\n
# @lcpr case=end

# @lcpr case=start
# ["How is leetcode for everyone","Leetcode is useful for practice"]\n["Bob","Charlie"]\n
# @lcpr case=end

#


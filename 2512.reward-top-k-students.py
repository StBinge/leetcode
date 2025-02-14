#
# @lc app=leetcode.cn id=2512 lang=python3
# @lcpr version=30204
#
# [2512] 奖励最顶尖的 K 名学生
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        vals={}
        for neg in negative_feedback:
            vals[neg]=-1
        for pos in positive_feedback:
            vals[pos]=3
        scores=[]
        for sid,re in zip(student_id,report):
            score=0
            for word in re.split():
                score+=vals.get(word,0)
            scores.append([sid,score])
        return [sid for sid,_ in heapq.nlargest(k,scores,key=lambda x:[x[1],-x[0]])]

# @lc code=end
assert Solution().topStudents(positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2)==[2,1]
assert Solution().topStudents(positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2)==[1,2]


#
# @lcpr case=start
# ["smart","brilliant","studious"]\n["not"]\n["this student isstudious","the student is smart"]\n[1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# ["smart","brilliant","studious"]\n["not"]\n["this student is notstudious","the student is smart"]\n[1,2]\n2\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=732 lang=python3
#
# [732] 我的日程安排表 III
#

# @lc code=start
class MyCalendarThree:

    def __init__(self):
        self.tree={}
    
    def update(self,start,end,l,r,idx):
        if end<l or start>r:
            return
        if start<=l and r<=end:
            node=self.tree.get(idx,[0,0])
            node[0]+=1
            node[1]+=1
            self.tree[idx]=node
            return
        mid=(l+r)//2
        self.update(start,end,l,mid,idx*2)
        self.update(start,end,mid+1,r,idx*2+1)
        node=self.tree.get(idx,[0,0])
        node[0]=node[1]+max(self.tree.get(idx*2,[0,0])[0],self.tree.get(idx*2+1,[0,0])[0])
        self.tree[idx]=node
    def book(self, startTime: int, endTime: int) -> int:
        self.update(startTime,endTime-1,0,10**9,1)
        return self.tree[1][0]



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
# @lc code=end


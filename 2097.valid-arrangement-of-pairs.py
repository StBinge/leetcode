#
# @lc app=leetcode.cn id=2097 lang=python3
# @lcpr version=30204
#
# [2097] 合法重新排列数对
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # N=len(pairs)
        # ends=defaultdict(list)
        # starts=defaultdict(list)
        # node_inputs=defaultdict(int)
        # node_outputs=defaultdict(int)
        nodes={}
        for i,[s,e] in enumerate(pairs):
            # starts[s].append(i)
            # ends[e].append(i)
            _,output=nodes.setdefault(s,[[],[]])
            output.append(e)
            input,_=nodes.setdefault(e,[[],[]])
            input.append(s)

        start_node=-1
        end_node=-1
        for node in nodes:
            input,output=nodes[node]
            if len(input)==0:
                start_node=node
                break
            if len(input)<len(output):
                start_node=node
            if len(output)==0:
                end_node=node
        if start_node==-1:
            start_node=pairs[0][0]
        ret=[]
        cur=start_node
        while True:
            output=nodes[cur][1]
            if not output:
                break
            mx_in=0
            target=output[0]
            for nxt in output:
                _in,_out=nodes[nxt]
                if len(_in)==1 and len(_out):
                    target=nxt
                    break
                if len(_in)>mx_in:
                    mx_in=len(_in)
                    target=nxt
            nxt=target
            output.remove(target)
      
            ret.append([cur,nxt])
            cur=nxt
        return ret


        
        
# @lc code=end
def check(args,answer=None):
    ret=Solution().validArrangement(args)
    if len(ret)!=len(args):
        ret_set=set(map(tuple,ret))
        missing=[]
        for s,e in args:
            if (s,e) not in ret_set:
                missing.append([s,e])            
        print(f'Error! length not equal! \nMissing:{missing}')
        return
    if sorted(args)!=sorted(ret):
        print(f'Error, nodes not match!\n{args}\n{ret}')
        return
    pre=ret[0][1]
    for s,e in ret[1:]:
        if pre!=s:
            print(f'Error, nodes not linked!\n{args}\n{ret}')
        pre=e


check([[5,13],[10,6],[11,3],[15,19],[16,19],[1,10],[19,11],[4,16],[19,9],[5,11],[5,6],[13,5],[13,9],[9,15],[11,16],[6,9],[9,13],[3,1],[16,5],[6,5]])
    


#
# @lcpr case=start
# [[5,1],[4,5],[11,9],[9,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[3,2],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[1,3],[2,1]]\n
# @lcpr case=end

#


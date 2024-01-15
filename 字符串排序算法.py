def LSD(strs:list[str]):
    """
    Every string of the list must have same length!
    String can include any ascii code.
    """
    N=len(strs)
    if N==0:
        return strs
    L=len(strs[0])
    R=256
    for cid in range(L-1,-1,-1):
        count=[0]*R
        for i in range(N):
            count[ord(strs[i][cid])+1]+=1
        for i in range(1,R):
            count[i]+=count[i-1]
        aux=['']*N
        for i in range(N):
            _ord=ord(strs[i][cid])
            aux[count[_ord]]=strs[i]
            count[_ord]+=1
        strs=aux
    return strs

from enum import Enum
class CharSet(Enum):
    Lower=1
    Upper=2

def MSD(strs:list[str]):
    R=128
    def sort(lo:int,hi:int,d:int):
        if lo>=hi:
            return
        # if d>(max(len(s) for s in strs[lo:hi+1])):
        #     return 
        counter=[0]*(R+2)
        for i in range(lo,hi+1):
            _ord=ord(strs[i][d]) if d<len(strs[i]) else -1
            _ord+=2
            counter[_ord]+=1
        if counter[1]==hi-lo+1:
            return

        for i in range(R+2):
            counter[i]+=counter[i-1]
        aux=['']*(hi-lo+1)
        for i in range(lo,hi+1):
            _ord=ord(strs[i][d]) if d<len(strs[i]) else -1
            _ord+=1
            rank=counter[_ord]
            counter[_ord]+=1
            aux[rank]=strs[i]
        for i in range(lo,hi+1):
            strs[i]=aux[i-lo]
        pre=0
        for i in range(R):
            sort(lo+pre,lo+counter[i]-1,d+1)
            pre=counter[i]
    
    sort(0,len(strs)-1,0)
    return strs

def generate_test_strs(str_len:int,str_count:int,same_str_len=True):
    import random
    strs=[]
    for _ in range(str_count):
        str=[]
        len=str_len
        if not same_str_len:
            len=random.randint(1,str_len)
        for i in range(len):
            while True:
                n=random.randint(0,127)
                ch=chr(n)
                if ch.isalnum():
                    str.append(ch)
                    break
        strs.append(''.join(str))
    return strs

def test_lsd(str_len,str_count,test_count):
    for _ in range(test_count):
        strs=generate_test_strs(str_len,str_count)
        ans=sorted(strs)
        ret=LSD(strs.copy())
        if ret!=ans:
            raise ('Test Failed with input:',strs)
    print('Test Passed!')

def test_msd(str_len,str_count,test_count):
    for i in range(test_count):
        print(f'Test {i+1}')
        strs=generate_test_strs(str_len,str_count,False)
        print('Origin strs:')
        print(strs)
        ans=sorted(strs)
        print('sorted strs:')
        print(ans)

        ret=MSD(strs.copy())
        print('MSD strs:')
        print(ret)
        if ret!=ans:
            raise 'Test Failed!'


if __name__ == '__main__':
    # test_lsd(6,10,10)
    test_msd(6,10,10)
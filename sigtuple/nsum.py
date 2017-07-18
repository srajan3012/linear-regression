def get_paths(curr_sum, A,S):
    if S <= A:
        if curr_sum+S == A:
            return 1
        if curr_sum+S > A:
            return 0
        else:
            curr_sum += S
        
        while I + S <= A:
            p += get_paths(curr_sum + S + I, A, S)
        # p2 = get_paths(curr_sum, A, S+1)
        # return p1+p2
        
    else:
        return 0


T = int(raw_input())

for i in range(T):
    A,S = map(int, raw_input().strip().split())
    
    if S < A:
        print get_paths(0,A,S)
    else:
        print 0
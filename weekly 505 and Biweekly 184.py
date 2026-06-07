################################################################
#                     weekly 505 contest                       #
################################################################

#Q1
class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        low = max(1, n-k)
        high = n+k
        total = 0
        for x in range (low, high+1):
            if (n & x)== 0:
                total+=x
        return total
        
#Q2
class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        res =[]
        cur =[]

        def backtrack (i:int, cost:int, prev_one:bool)-> None:
            if i ==n:
                res.append("".join(cur))
                return
            cur.append('0')
            backtrack(i+1, cost, False)
            cur.pop()

            if not prev_one and cost +i <=k:
                cur.append('1')
                backtrack(i+1, cost+i, True)
                cur.pop()
        
        backtrack(0,0,False)
        return res
        
#Q3
class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        NEG = float ('-inf')

        #Prefix
        P = [0]* (n+1)
        for i in range (n):
            P[i+1] = P[i] + nums[i]

        #dp0
        #dp0 = [[0]* (m+1) for _ in range (n+1)]
        #dp1 = [[NEG] * (m+1) for _ in range (n+1)]
        dp0_prev = [0]* (n+1)
        dp1_prev = [NEG]*(n+1)

        for j in range (1, m+1):
            G = [P[k] + dp0_prev[k] for k in range(n+1)]

            wmax = [NEG] * n
            dq = deque()
            add=0
            for i in range(n):
                hi = min(i+r, n)
                lo = i+l
                while add<=hi:
                    while dq and G[dq[-1]] <= G[add]:
                        dq.pop()
                    dq.append(add)
                    add+=1
                while dq and dq[0] <lo:
                    dq.popleft()
                if dq and lo <=hi:
                    wmax[i] = G[dq[0]]


            dp0 = [0]*(n+1)
            dp1 = [NEG] * (n+1)
            for i in range (n-1, -1, -1):
                take = wmax[i] - P[i] if wmax[i] != NEG else NEG
                dp0[i] = max(dp0[i+1], take)
                dp1[i] = max(dp1[i+1], take)

            dp0_prev, dp1_prev = dp0, dp1

        return dp1_prev[0]
#Q4
# the code exceeded time limit but passed 989/000 test cases
class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        NEG = float('-inf')
        m = min(m, n //l)
        P= [0]*(n+1)
        for i in range (n):
            P[i+1] = P[i] +nums[i]

        dp0_prev = [0] *(n+1)
        #dp1_prev = [NEG]*(n+1)
        ans = NEG

        for j in range (1, m+1):
            G = [P[k] + dp0_prev[k] for k in range(n+1)]
            wmax = [NEG] * (n+1)
            dq = deque()

            for i in range(n, -1,-1):
                lo = i+l
                hi = i+r
                if lo <= n and G[lo]!= NEG:
                    while dq and G[dq[-1]] <= G[lo]:
                        dq.pop()
                    dq.append(lo)

                
                while dq and dq[0]> hi:
                    dq.popleft()
                if dq:
                    wmax[i] = G[dq[0]]

            dp0 = [NEG] *(n+1) 
            #dp1 = [NEG] *(n+1)
            for i in range (n-1, -1, -1):
                take = wmax[i] - P[i] if wmax[i] != NEG else NEG
                dp0[i] = max (dp0[i+1], take)
                #dp1[i] = max (dp1[i+1], take)
            dp0_prev = dp0
            ans = max(ans,dp0_prev[0])

        return ans

#################################################################
#                      Biweekly 184 contest                     #
#################################################################

#Q1
class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        pair = n & (n>>1)
        if (bin(pair).count('1')==1):
            return True
        else: return False
#Q2
class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        #
        if brightness == 0 or not intervals:
            return 0
        bulbs = (brightness +2)//3
        intervals.sort()
        total_units = 0
        curStart, curEnd = intervals[0]
        for s, e in intervals[1:]:
            if s<=curEnd:
                curEnd= max(curEnd, e)
            else:
                total_units += curEnd - curStart+1
                curStart, curEnd = s, e
        total_units += curEnd - curStart +1
        return bulbs*total_units
#Q3
class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        n = len(nums)
        total =0
        i=0
        while i<n:
            if s[i] =='0':
                i+=1
                continue
            a=i
            while i<n and s[i] == '1':
                i+=1
            b = i-1
            if a ==0:
                total += sum (nums[0:b+1])
            else: 
                window = nums[a-1:b+1]
                total += sum (window) - min(window)
        return total
#Q4

class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        n = len(nums)
        cur = set(nums)
        items = list(Counter(nums).items())
        best = float('-inf')
        lo = max (1, maxVal -n - 2)
        for v in range (maxVal, lo-1, -1):
            if v+1<= best:
                break
            b = sum(f for x, f in items if gcd(x,v)!= 1)
            if v>1 and v in cur:
                m=1
            elif b>= 1 or (v==1 and 1 in cur):
                m=0
            else:
                m=-1
            best = max(best, v-b+m)
        for v in sorted((u for u in cur if u > maxVal), reverse = True):
            if v<=best:
                break
            b = sum(f for x, f in items if gcd(x,v)!= 1)
            best = max(best, v-b+1)
        return best

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i, curr, n = 0, 0, len(gas)
        target = n+1
        delta = [gas[i]-cost[i] for i in range(n)]
        if sum(delta)<0: return -1
        while True:
            j = i%n
            curr+=delta[j]; target-=1
            if curr<0: target=n+1; curr=0
            if target==0: return j
            i+=1
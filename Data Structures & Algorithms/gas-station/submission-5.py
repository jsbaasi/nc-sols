class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i, res, curr, n = 0, 0, 0, len(gas)
        target = n+1
        delta = [gas[i]-cost[i] for i in range(n)]
        if sum(delta)<0: return -1
        for i in range(n):
            curr += delta[i]
            if curr<0: res = i+1; curr = 0
        return res
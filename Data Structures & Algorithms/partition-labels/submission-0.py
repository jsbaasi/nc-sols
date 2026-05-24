class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        tracking = set()
        run = 1
        res = []
        for c in s:
            tracking.add(c)
            count[c]-=1
            if count[c]==0: tracking.remove(c)
            if not tracking: res.append(run); run = 1
            else: run+=1
        return res
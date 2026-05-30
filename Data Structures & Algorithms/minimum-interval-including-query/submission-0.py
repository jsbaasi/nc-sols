class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        for all query numbers:
        given a number, find the length of the smallest interval that contains it
        '''
        res = []
        for q in queries:
            curr = 10001
            for start, end in intervals:
                if start <= q <= end and end-start+1<curr: curr = end-start+1
            res.append(curr if curr<10001 else -1)
        return res
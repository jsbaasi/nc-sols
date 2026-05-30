class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        for all query numbers:
        given a number, find the length of the smallest interval that contains it
        '''
        upper = 10001
        sweep = [upper]*(upper)
        for start, end in intervals:
            l = end-start+1
            for i in range(start, end+1):
                sweep[i] = min(sweep[i], l)
        return [sweep[q] if sweep[q]<upper else -1 for q in queries]
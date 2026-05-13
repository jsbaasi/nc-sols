class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        the longest is len(nums)
        intervals question it seems like
        can we keep track of just the ends and starts

        starts=2,20,4,10 ends=20,5,10
        if x-1 in ends: remove(x-1) and add(x) if (x+1) doesn't exist
        if x+1 in starts: remove(x+1) and add(x) if (x-1) doesn't exist
        this doesn't keep starts and ends in sync, e.g if 4 is removed from
        ends then it's still in starts
        this doesn't help us get the length either, as we don't know what start
        links to what end?
        '''
        n = len(nums)
        chains = []
        for i in range(n):
            added_start = (False, -1)
            added_end = (False, -1)
            curr_number = nums[i]
            for j in range(len(chains)):
                start, end = chains[j]
                if curr_number==start or curr_number==end: continue
                if start==curr_number+1:
                    chains[j][0] = curr_number
                    added_start = (True, j)
                if end==curr_number-1:
                    chains[j][1] = curr_number 
                    added_end = (True, j)
            if added_start[0] and added_end[0]:
                _, new_end = chains[added_start[1]]
                chains[added_end[1]][1] = new_end
                chains.pop(added_start[1])
            elif not added_start[0] and not added_end[0]:
                chains.append([curr_number, curr_number])
        largest = 0
        for start, end in chains:
            largest = max(end-start+1, largest)
        return largest
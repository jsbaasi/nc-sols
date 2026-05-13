class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        we have a hashmap that maps boundaries to sequence length
        '''
        longest = 0
        n_map = defaultdict(int)
        for n in nums:
            if not n_map[n]:
                start_length = n_map[n-1] if n-1 in n_map else 0
                end_length = n_map[n+1] if n+1 in n_map else 0
                length = start_length + 1 + end_length
                n_map[n-start_length] = max(n_map[n-start_length], length)
                n_map[n+end_length] = max(n_map[n-end_length], length)
                n_map[n] = length
                print(n, length)
                longest = max(longest, length)
        return longest
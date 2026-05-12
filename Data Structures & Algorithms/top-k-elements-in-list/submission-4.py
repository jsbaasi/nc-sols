class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket_sort = [[] for _ in range(n+1)]
        count = defaultdict(int)
        for curr in nums:
            count[curr]+=1
        for curr, cnt in count.items():
            bucket_sort[cnt].append(curr)
        res = []
        print(bucket_sort)
        for i in range(n, -1, -1): # n=2, bucket sort looks like 0 1 2 so i want 2 1 0
            print(i)
            curr = bucket_sort[i]
            res += curr
            if len(res)==k: return res
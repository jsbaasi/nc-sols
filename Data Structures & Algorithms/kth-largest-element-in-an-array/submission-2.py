class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        bucket sort normally used for frequency, where the frequency
        of an element is the key for the bucket, so it's o(n) time complexity
        which is only used when the max is constrained as the frequency is
        (frequency can't exceed length of array) but the largest number is not
        constrained here, it oculd be large af, so it would be large af bucket
        sort array, in this case only one element belongs to each bucket so
        it could be an array of booleans, and then we iterate backwards
        to find the kth True value
        2,3,1,1,5,5,4
        sorting sol:
        tc > nlogn
        sc > n
        heap sol:
        tc > klogn
        sc > n
        bucket sol:
        tc > max(n, largest_number)
        sc > max(n, largest_number)
        if largest number is quite large then would be less efficient than klogn
        '''
        key = -1*min(nums)
        n = max(nums)+key+1
        buckets = [0] * n
        for num in nums:
            buckets[num+key]+=1
        for i in range(n-1, -1, -1):
            if buckets[i]: k-=buckets[i]
            if k<=0: return i-key
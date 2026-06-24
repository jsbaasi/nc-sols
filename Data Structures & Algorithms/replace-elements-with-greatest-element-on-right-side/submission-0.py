class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        largest = -1
        for i in range(n-1, -1, -1):
            tmp = arr[i]
            arr[i] = largest
            largest = max(largest, tmp)
        return arr
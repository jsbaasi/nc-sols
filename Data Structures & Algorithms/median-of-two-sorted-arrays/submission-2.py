class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)<len(nums2): nums1,nums2=nums2,nums1 # nums1 is bigger
        n,m = len(nums1), len(nums2)
        if not nums2:
            if n%2==0: return (nums1[n//2-1] + nums1[n//2])/2
            else: return nums1[n//2]
        l_n, r_n = -1, n

        for _ in range(20):
            n_pivot = (l_n+r_n)//2
            m_pivot = (m+n)//2-n_pivot-1
            print(n_pivot, m_pivot)
            i = nums1[n_pivot] if 0<=n_pivot<n else (-float("inf") if n_pivot==-1 else float("inf"))
            j = nums1[n_pivot+1] if 0<=n_pivot+1<n else (-float("inf") if n_pivot+1==-1 else float("inf"))
            k = nums2[m_pivot] if 0<=m_pivot<m else (-float("inf") if m_pivot==-1 else float("inf"))
            l = nums2[m_pivot+1] if 0<=m_pivot+1<m else (-float("inf") if m_pivot+1==-1 else float("inf"))
            print(f"[error]: i={i},j={j},k={k},l={l}")
            if i<=k<=j or k<=i<=l:
                print("here")
                if (m+n)%2==0:
                    return (i+k)/2
                else:
                    if i<=k<=j:
                        return float(k)
                    elif k<=i<=l:
                        return float(i)
            elif (i<k and i<l): l_n = n_pivot+1
            elif (i>k and i>l): r_n = n_pivot-1

            # else: print(f"[error]: i={i},j={j},k={k},l={l}")
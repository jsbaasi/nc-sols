class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        'aaabbbccc'
        '''
        res = []

        '''
        we don't have to keep 2 pointers if maintain an invariant
        the entire way through, if we say everything before i is already a perm
        then iterate forwards from i and make more perms, if i reaches the end
        then we have made perm splits of the entire string and we append to res
        '''
        n = len(s)

        def is_perm(st: str) -> bool:
            l, r = 0, len(st)-1
            while l<r:
                if st[l]==st[r]: l+=1;r-=1;
                else: return False
            return True

        def dfs(i, curr):
            if i>=n: res.append(curr.copy())

            for j in range(i, n):
                if is_perm(s[i:j+1]): curr.append(s[i:j+1]); dfs(j+1, curr); curr.pop()

        dfs(0, [])
        return res
        
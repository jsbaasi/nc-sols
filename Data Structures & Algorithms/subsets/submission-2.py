class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in nums:
            curr = []
            for ss in subsets:
                adding_to_this_list = ss.copy()
                adding_to_this_list.append(n)
                curr.append(adding_to_this_list)
            subsets+=curr

        return subsets

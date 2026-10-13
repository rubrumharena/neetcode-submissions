class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        i = 0
        for num in nums:
            seen = set()
            for sub_num in nums[i + 1:]:
                need = -num - sub_num
                if need in seen:
                    res.add(tuple(sorted((num, sub_num, need))))
                seen.add(sub_num)
            i += 1
        return [list(t) for t in res]
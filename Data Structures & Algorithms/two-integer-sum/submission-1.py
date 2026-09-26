class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        i = 0
        for num in nums:
            ht[target - num] = i
            i += 1

        j = 0
        for num in nums:
            half = ht.get(num)
            if half is None or half == j:
                j += 1
                continue
            break

        return [j, half]
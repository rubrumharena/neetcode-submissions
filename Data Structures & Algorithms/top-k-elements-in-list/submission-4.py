class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht1 = {}
        for num in nums:
            ht1[num] = ht1.get(num, 0) + 1

        ht2 = {}
        for num, count in ht1.items():
            ht2.setdefault(count, []).append(num)

        res = []
        for count in sorted(ht2, reverse=True):
            for num in ht2[count]:
                res.append(num)
                if len(res) == k:
                    return res
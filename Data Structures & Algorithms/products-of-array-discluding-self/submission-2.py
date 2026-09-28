class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        base_product = 0
        zero_count = 0
        for num in nums:
            if num != 0:
                if base_product == 0:
                    base_product = 1
                base_product *= num
            else:
                zero_count += 1

        res = []
        for num in nums:
            if zero_count > 1:
                res.append(0)
            elif num == 0:
                res.append(base_product)
            elif zero_count == 1:
                res.append(0)
            else:
                res.append(int(base_product / num))
        return res
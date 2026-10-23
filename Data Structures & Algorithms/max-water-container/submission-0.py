class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        sq = 0
        while r != l:
            rh = heights[r]
            lh = heights[l]
            cur_sq = min(rh, lh) * (r - l)
            sq = cur_sq if cur_sq > sq else sq

            if lh < rh:
                l += 1
            else:
                r -= 1
        
        return sq

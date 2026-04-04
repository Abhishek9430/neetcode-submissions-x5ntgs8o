class Solution:
    def trap(self, height: List[int]) -> int:
        # min(lh,rh)-height[i]

        lh = height[0]
        rh = height[-1]
        i = 0
        j = len(height)-1
        area = 0
        while i < j:
            if lh < rh:
                area += lh - height[i]
                i += 1
                lh = max(lh,height[i])
            elif lh >= rh:
                area += rh - height[j]
                j -= 1
                rh = max(rh,height[j])
        return area

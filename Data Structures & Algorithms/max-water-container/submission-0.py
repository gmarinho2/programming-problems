class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights)-1
        while left < right:
            smallest_side = min(heights[left], heights[right])
            area = (right - left) * smallest_side
            if area > max_area:
                max_area = area
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1

        return max_area
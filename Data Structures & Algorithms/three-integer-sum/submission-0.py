class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, number in enumerate(nums):
            if number > 0:
                break
            if i > 0 and number == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                summation = nums[left] + nums[right] + number
                if summation < 0:
                    left+=1
                elif summation > 0:
                    right-=1
                else:
                    result.append([nums[left], nums[right], number])
                    left += 1
                    right -=1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result
                

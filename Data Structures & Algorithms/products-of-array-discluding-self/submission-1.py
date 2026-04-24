class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [0] * len(nums)
        acumulado = acumulado2 = 1
        zeros = 0
        for number in nums:
            acumulado2 *= number
            if number != 0:
                acumulado *= number
            else:
                zeros += 1
                if zeros >= 2:
                    acumulado *= number
        for i in range(len(nums)):
            if nums[i]!=0:
                products[i] = int(acumulado2 / nums[i])
            else:
                products[i] = acumulado
        return products
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

#QUESTION:
#Given an integer array nums, return an array output where output[i] is 
#the product of all the elements of nums except nums[i].
#Each product is guaranteed to fit in a 32-bit integer.
#Follow-up: Could you solve it in O(n)O(n) time without using the division operation?
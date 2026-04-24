class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequent = []
        for i in range(k):
            maior = 0
            element = 0
            for number in nums:
                quantity = 0
                for number2 in nums:
                    if number2 == number:
                        quantity += 1
                if quantity > maior:
                    maior = quantity
                    element = number
            most_frequent.append(element)
            for i in range(maior):
                nums.remove(element)
        return most_frequent

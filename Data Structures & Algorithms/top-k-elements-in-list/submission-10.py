class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lista = []
        for iterations in range(k):

            mais_frequente = 0
            frequencia = 0
            for numero in nums:
                quantidade = 0
                for num2 in nums:
                    if num2 == numero:
                        quantidade += 1
                if quantidade > frequencia:
                    frequencia = quantidade
                    mais_frequente = numero

            lista.append(mais_frequente)
            for i in range(frequencia):
                nums.remove(mais_frequente)
        return lista
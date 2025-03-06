class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lista_diferencas = []
        for index, numero in enumerate(nums):
            atual_diff = numero - target
            lista_diferencas.append(atual_diff)
        
        i = 0
        j = 1
        if lista_diferencas[0] >= 0:
            return 0
        
        elif lista_diferencas[-1] < 0:
            return len(lista_diferencas)
        
        elif lista_diferencas[-1] == 0:
            return len(lista_diferencas) - 1

        while True:

            if lista_diferencas[i] < 0 and lista_diferencas[j] >= 0:
                return j
            
            else:
                i += 1
                j += 1
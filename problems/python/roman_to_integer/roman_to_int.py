class Solution:
    def romanToInt(self, s: str) -> int:
        romain = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        valor_anterior = 0

        for i in reversed(s):
            valor_atual = romain[i]

            if (valor_atual < valor_anterior):
                total -= valor_atual
            else:
                total += valor_atual
            valor_anterior = romain[i]

        return total

"""🧠 Exercício: Sistema de Controle de Estoque
Crie uma classe chamada  que represente um item em um estoque. Cada produto deve ter:
• 	 (string)
• 	 (float)
• 	 (int)
🧰 Requisitos:
1. 	Um método  que imprime as informações do produto.
2. 	Um método  que aumenta a quantidade.
3. 	Um método  que diminui a quantidade, mas não permite que fique negativo.
4. 	Um método  que retorna o valor total em estoque (preço × quantidade)."""

class estoque:
    def __init__(self, nome, quantidade, estoque):
        self.nome = nome
        self.quantidade= quantidade
        self.estoque = estoque

    def __str__(self):
        return f"O produto é {self.nome}. Ele tem em estoque: {self.estoque}"


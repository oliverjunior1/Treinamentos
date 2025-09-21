class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def imprimir_informacoes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço unitário: R${self.preco:.2f}")
        print(f"Quantidade em estoque: {self.quantidade}")

    def adicionar_estoque(self, quantidade_adicional: int):
        if quantidade_adicional > 0:
            self.quantidade += quantidade_adicional
        else:
            print("Quantidade inválida para adicionar.")

    def remover_estoque(self, quantidade_removida: int):
        if 0 < quantidade_removida <= self.quantidade:
            self.quantidade -= quantidade_removida
        else:
            print("Não é possível remover essa quantidade do estoque.")

    def valor_total_estoque(self) -> float:
        return self.preco * self.quantidade

produto = Produto("Microcomputador", 15.99, 25)

print(f"O produto {produto.nome}, custa {produto.preco} e tem {produto.quantidade}")



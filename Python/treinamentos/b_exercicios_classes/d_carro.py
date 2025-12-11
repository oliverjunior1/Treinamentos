class Carro:
    def __init__(self, marca, modelo, ano, velocidade_atual):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade_atual = velocidade_atual

    def acelerar(self):
        self.velocidade_atual += 2
        return self.velocidade_atual

    def frear(self):
        self.velocidade_atual -= 2
        return self.velocidade_atual

    def __str__(self):
        return (f"Marca do carro:{self.marca}"
                f"Modelo do carro:{self.modelo}"
                f"Ano do carro: {self.ano}"
                f"Velocidade atual: {self.velocidade_atual}")



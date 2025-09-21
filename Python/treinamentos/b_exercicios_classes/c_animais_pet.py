class Pet:
    def __init__(self, nome, especie, idade, peso):
        self.nome = nome
        self.especie = especie.lower()
        self.idade = idade
        self.peso = peso

    def exibir_info(self):
        print(f"\n🐾 Informações do Pet:")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso:.2f} kg")

    def alimentar(self):
        peso_comida = float(input("Qual o peso da comida em kg? "))
        self.peso += peso_comida
        print(f"{self.nome} foi alimentado. Novo peso: {self.peso:.2f} kg")

    def aumentar_idade(self):
        self.idade += 1
        print(f"{self.nome} agora tem {self.idade} anos.")

    def saude(self):
        faixas = {
            "gato": (2, 10),
            "cachorro": (2, 10),
            "coelho": (2, 10),
            "cavalo": (10, 40),
            "vaca": (10, 40)
        }

        if self.especie in faixas:
            minimo, maximo = faixas[self.especie]
            if self.peso < minimo:
                print(f"{self.nome} está abaixo do peso. 🥺")
            elif self.peso > maximo:
                print(f"{self.nome} está acima do peso. 🐷")
            else:
                print(f"{self.nome} está com peso saudável. ✅")
        else:
            print("Não há dados suficientes para avaliar a saúde dessa espécie.")

cachorro = Pet("lassie", 'cachorro', 5,1.5)
cachorro.saude()
cachorro.alimentar()
cachorro.saude()

cavalo = Pet("mulambo", "cavalo", 14,9)
cavalo.saude()
cavalo.exibir_info()
cavalo.alimentar()
cavalo.aumentar_idade()
cavalo.saude()
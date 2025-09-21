# 🐶 Exercício: Classe Pet
# Crie uma classe chamada Pet que represente um animal de estimação. Cada pet deve ter:
#
# 🧰 Requisitos:
class Pet:
    def __init__(self,nome, especie, idade, peso):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso

# 1. 	Um método  que imprime todos os dados do pet.
    def exibir_info(self):
        return (f"O animal {self.especie}\n"
                f"tem nome de : {self.nome}\n"
                f"tem a idade de: {self.idade}\n"
                f"e tem o peso de: {self.peso}.")

# 2. 	Um método  que aumenta o peso do pet.
    def alimentar(self):
        peso_comida = float(input("Qual o peso da comida em kilos:"))
        self.peso+= peso_comida
        return self.peso

# 3. 	Um método  que aumenta a idade em 1 ano.
    def aumentar_idade(self):
        self.idade += 1
        return self.idade

# 4. 	Um método  que avalia a saúde do pet com base
# no peso e espécie (ex: se for um gato com menos de
# 2kg, está abaixo do peso).

    def saude(self):
        if self.especie=="gato" or "cachorro" or "coelho":
            if self.peso<2:
                return (f"O {self.especie} não está saudável,\n"
                        f"dê mais comida a ele.")
            elif self.peso>10:
                return (f"O {self.especie} não está saudável\n "
                        f"reduza a comida que ele está comendo.")
            else:
                return f"O animal {self.especie} está saudavel."
        elif self.especie=="cavalo" or "vaca":
            if self.peso<10:
                return (f"O {self.especie} não está saudável."
                        f"dê mais comida a ele.")
            elif self.peso>40:
                return (f"O {self.especie} naõ está saudável."
                        f"reduza a comida dele.")
            else:
                return ("O animal está saudável.2")

        else:
            return "Não há dados para este animal."

gato = Pet("fofa", "gato", 3, 3)

print(gato.saude())
cavalo = Pet("pangaré", "cavalo", 10,7)
print(cavalo.saude())

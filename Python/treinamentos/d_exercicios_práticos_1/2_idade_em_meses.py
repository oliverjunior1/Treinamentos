idade = int(input("Coloque a sua idade: "))
meses_faltando = int(input("Coloque quantos meses faltam para o seu aniversário: "))

# meses vividos neste ano = 12 - meses_faltando
meses_vividos = 12 - meses_faltando  

print(f"Você tem {idade * 12 + meses_vividos} meses de vida.")

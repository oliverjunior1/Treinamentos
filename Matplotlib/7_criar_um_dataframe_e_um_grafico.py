# Criar um pequeno conjunto de dados com pandas e gerar um gráfico simples com matplotlib.

# 🎯 Cenário
#
# Você tem as vendas de uma loja durante 5 dias:
#
# Dia	Vendas
# 1	100
# 2	150
# 3	130
# 4	170
# 5	160
# ✅ Tarefas
#
# Crie um DataFrame com esses dados usando pandas.
#
# Mostre o DataFrame na tela.
#
# Gere um gráfico de linha mostrando a evolução das vendas.
#
# Coloque:
#
# Título: "Vendas da Semana"
#
# Nome no eixo X: "Dia"
#
# Nome no eixo Y: "Vendas"
#
# 🚀 Desafio extra (opcional)
#
# Calcule a média das vendas.
#
# Mostre essa média como uma linha horizontal no gráfico.

import pandas as pd
import matplotlib.pyplot as plt

# Crie um DataFrame com esses dados usando pandas.
x = pd.DataFrame({'dia':[1,2,3,4,5],'vendas':[100,150,130,170,160]})

# Mostre o DataFrame na tela.
print(x)

# Gere um gráfico de linha mostrando a evolução das vendas.
plt.plot(x['dia'], x['vendas'])

# Título: "Vendas da Semana"
plt.title("Vendas da Semana")

# Nome no eixo X: "Dia"
plt.xlabel('Dia')

# Nome no eixo Y: "Vendas"
plt.ylabel('Vendas')

# Calcule a média das vendas.
media_das_vendas = sum(x['vendas'])/len(x['vendas'])
print(media_das_vendas)

# Mostre essa média como uma linha horizontal no gráfico.
plt.figtext(0.5,0.2,f"A media das vendas foi: {media_das_vendas}.", ha='center')

plt.show()

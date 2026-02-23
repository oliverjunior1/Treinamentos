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

dados = {'dia':[1,2,3,4,5],
         'vendas':[100,150,130,170,160]}

x = pd.DataFrame(dados)

plt.plot(x)
plt.show()
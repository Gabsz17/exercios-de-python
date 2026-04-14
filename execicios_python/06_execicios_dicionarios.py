# EXECÍCIO 01 - Atualização de Cadastro de Clientes

# #Dicionário de clientes
# clientes = {"Lira": 5000, "Alon": 3000, "Julia": 4500}
# #Atualizando valor de Alon
# clientes["Alon"] += 1500
# #Adionando novo cliente
# clientes["Marcos"] = 2000
# # #Gerando relatórios
# for nome, valor in clientes.items():
#     print(f"Cliente {nome} -- Saldo: R${valor}")

# EXECÍCIO 02 - Consulta de Estoque Interativa

# estoque = {"teclado": 50, "mouse": 120, "monitor": 30}
# produto = input("Digite o nome de um produto: ")
# produto_estoque = produto.strip().lower()
# if produto_estoque in estoque:
#     quantidade = estoque[produto_estoque]
#     print(f"Existem {quantidade} de {produto_estoque} no estoque!")
# else:
#     print  (f"Produto não encontrado no sistema")

# EXERCÍCIO 03 - Análise de Faturamento por Região

# vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}
# total_faturamento = sum(vendas_regiao.values())
# quantidade_regioes = len(vendas_regiao)
# media_faturamento = total_faturamento / quantidade_regioes
# for regiao, faturamento in vendas_regiao.items():
#     print (f"A região {regiao} faturou {faturamento}")
# print (f"O faturamento total foi de: {total_faturamento}")
# print (f"A média de faturamento das regiões foi de: {media_faturamento}")

# EXERCÍCIO 04 -  Média de Desempenho 

desempenho = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}
print ("As notas de Paula foram: ", desempenho["Paula"])
total_notas = sum(desempenho["Paula"])
media_notas = sum(desempenho["Paula"]) / len(desempenho["Paula"])
print (f"As notas de Paula foram {desempenho['Paula']}")
print (f"A soma das motas de paula é: {total_notas}")
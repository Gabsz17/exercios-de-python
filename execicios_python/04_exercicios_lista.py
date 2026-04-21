#EXERCÍCIO 01 - Dashboard de Vendas

# vendas = [1500, 2000, 800, 3500, 1200]
# quantidade_vendas = len(vendas)
# total_vendas = sum(vendas)
# media_vendas = total_vendas / quantidade_vendas
# maior_vendas = max(vendas)
# menor_venda = min(vendas)
# print (f"--------------RELATÓRIO DE VENDAS-----------------")
# print (f"Total de vendas na semana: {total_vendas}")
# print (f"Média de vendas: {media_vendas}")
# print (f"Maior venda: R${maior_vendas}")
# print (f"Menor venda: R${menor_venda}")
# print ("--------------------------------------------------")

#EXERCÍCIO 02 - Gestão de Estoque

# estoque = ["monitor", "teclado", "mouse", "headset"]
# estoque.append("webcam")
# estoque[1] = "teclado mecânico"
# estoque.remove("mouse")
# if 'impressora' in estoque:
#     print("Impressora está no estoque")
# else:
#     print("Impressora não está no estoque")
# print (estoque)

#EXERCÍCIO 03 - Organização de Preços

# fretes = [50, 80, 20, 150, 40]
# fretes.sort(reverse=True)
# top_fretes = fretes[0:2]
# print (f"Fretes de forma ordenada: {fretes}")
# print (f"Top 2 fretes mais caros: {fretes}")

# #EXERCÍCIO 04 -  Sistema de Logística

rota_atual = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]
novas_cidades =  ["Itu", "Valinhos"]
rota_atual.extend(novas_cidades)
sorocaba = rota_atual.index("Sorocaba")
print (f"A nova rota do onibûs é: {rota_atual}")
print (f"Sorocaba é a {sorocaba + 1}ª cidade da rota")

#EXERCÍCIO 05
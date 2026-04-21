#EXERCÍCIO 01 - Cálculo de Bônus de Vendas

faturamento = 50000
percentual_bonus = 0.10
bonus = faturamento * percentual_bonus
faturamento_final = faturamento - bonus
print (f"O bonus para os funcionários é de: R${bonus}. O faturamento final da empresa é de: R${faturamento_final}")

#EXERCÍCIO 02 - Controle de Estoque

estoque = 250
vendas = 78
chegou_estoque = 100
final = estoque - vendas + chegou_estoque
print (f"A quantidade final de celulares é: {final}")

#EXERCÍCIO 03 -  Divisão de Cargas

caixas = 1250
caminhoes = 12
caminhoes_cheios = caixas // caminhoes
sobra = caixas % caminhoes
print (f"{caminhoes_cheios} caixas vão em caminhões cheios, sobrou {sobra} caixas que serão levados em uma viagem menor")

#EXERCÍCIO 04 - Análise de Margem de Lucro

faturamento = 15000
custos = 5000
imposto = 0.15
valor_imposto = faturamento * imposto
lucro_liquido = valor_imposto - custos
margem_lucro = lucro_liquido / faturamento
meta_atingingida = margem_lucro > 0.30
print (f"A margem de lucro foi: {margem_lucro:.2%}")
print (f"A meta foi atingida? {meta_atingingida}")

#EXERCÍCIO 05 - Conversão de Tempo

duracao = 40
anos = 40 // 12
meses = 40 % 12
print (f"O contrato tem duração de {anos} anos e {meses} meses")

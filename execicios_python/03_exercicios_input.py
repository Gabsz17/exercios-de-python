#EXERCÍCIO 01 - Calculadora de Imposto sobre Vendas

valor_bruto = input("Digite o valor bruto: R$")
valor_limpo = valor_bruto.replace(".", "").replace(",", ".").strip()
valor_decimal = float(valor_limpo)
imposto =  valor_decimal * 0.15
print (f"O valor do imposto é de: R${imposto:,.2f}")

#EXECÍCIO 02 - Sistema de Cadastro de Colaborador

nome = input("Digite o seu nome: ")
email = input("Digite o seu email: ")
nome_separado = nome.split()
primeiro_nome = nome_separado[0]
nome_formatado = primeiro_nome.capitalize()
email_padronizado =  email.lower().strip()
print (f"Cadastro concluído: {nome_formatado}. Email de acesso: {email_padronizado}")

#EXERCÍCIO 03 - Analise de Metas de Vendas

faturamento_loja_a = input("Digite o faturamento da loja A: R$")
faturamento_loja_b = input("Digite o faturamento da loja B: R$")
faturamento_formatado_loja_a = faturamento_loja_a.replace(".", "").replace(",", ".").strip()
faturamento_formatado_loja_b = faturamento_loja_b.replace(".", "").replace(",", ".").strip()
loja_a = float(faturamento_formatado_loja_a)
loja_b = float(faturamento_formatado_loja_b)
faturamento_total = loja_a + loja_b
media_faturamento = faturamento_total / 2
print (f"O faturamento total das duas lojas foi de: R${faturamento_total:,.2f}. A média de faturamento foi de: R${media_faturamento:,.2f}")
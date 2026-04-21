#EXERCÍCIO 01 -  Relatório de Margem de Lucro

# faturamento = float(45000)
# custo = float(23500)
# lucro = faturamento - custo
# margem_lucro = lucro / faturamento
# print (f"O lucro foi de de: R${lucro:,.2f}. A margem de lucro foi: {margem_lucro:.0%}")

#EXERCÍCIO 02 - Padronização de Dados de CRM

# nome = "mArCoS aNtOnIo rocHa"
# email = "MARCOS. ROCHA@GMAIL.COM"
# nome_formatado = nome.strip().title()
# email_formatado = email.replace(" ", "").lower()
# print (f"Nome: {nome_formatado}")
# print (f"Email: {email_formatado}")

#EXERCÍCIO 03 - Migracao de Servidor de E-mail

# email =  "andre_silva@empresa.com.br"
# email_novo = email.replace("empresa.com.br", "grupocorp.com")
# print (f"Antigo endereço de email: {email}. Novo endereço de email: {email_novo}")

#EXERCÍCIO 04 - Extracao de Username para Log

# email = "beatriz.oliveira@grupocorp.com"
# posicao_arroba = email.find("@")
# usuario =  email[0:posicao_arroba]
# print (f"O usuário extarido é: {usuario}")

#EXERCÍCIO 05 - Personalizacao de E-mail de Marketing

nome = " lucas ferreira souza"
nome_lista = nome.split()
primeiro_nome = nome_lista[0].capitalize()
print (f"olá, {primeiro_nome}")
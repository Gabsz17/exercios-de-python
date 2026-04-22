#EXERCÍCIO 01 - Validação de Investimento

# investimento = input("Digite o valor deseja investir: R$")
# valor_limpo = investimento.replace(".", "").replace(",", ".").strip()
# valor_limpo = float(valor_limpo)
# if valor_limpo < 1000:
#     print("Perfil iniciante: sugerimso Tesouro Direto")
# elif valor_limpo <= 5000:
#     print("'Perfil moderado: Sugerimos Fundos Imobiliários")
# else:
#     print("Perfil arrojado: Sugerimos Ações")

#EXERCÍCIO 02 - Controle de Acesso

# admins = ['ana@empresa.com', 'guilherme@empresa.com', 'felipe@empresa.com']
# email = input("Digite o seu email: ")
# email_padronizado = email.strip().lower
# if email_padronizado in admins:
#     print("Acesso liberado!")
# else:
#     print("Acesso negado.")

#EXERCÍCIO 03 - Cálculo de Desconto Progressivo

compras = float(input("Digite o valor de suas compras: R$"))
if compras >=500:
    desconto1 = compras * 0.85
    print(f"Parabéns! Você ganhou 15% de desconto.")
    print(f"Valor da sua compra agora é de: R${desconto1:,.2f}")
#Fazer a importação da biblioteca necessária
import re

#Criar um dicionário contendo as notas geradas pelo teste fictício
notasCandidatos = {
    1: "e9_t8_p7_s9",
    2: "e8_t8_p7_s3",
    3: "e6_t9_p9_s10",
    4: "e7_t5_p4_s5",
    5: "e3_t10_p10_s5",
}

# Padrão da expressão regular com X como um espaço reservado para a avaliação para localizar
# na string padrão, as notas atribuídas a cada parte da avaliação
padrao = r'e(\d+)_t(\d+)_p(\d+)_s(\d+)'

# Criar o loop para que possa ser pesquisado quantas vezes for necessário
while True:
  # Solicitar as notas de corte para a pesquisa
    cortEntrev = int(input("Digite a nota mínima para a entrevista (e): "))
    cortTeor = int(input("Digite a nota mínima para o teste teórico (t): "))
    cortPrat = int(input("Digite a nota mínima para o teste prático (p): "))
    cortSoft = int(input("Digite a nota mínima para as soft skills (s): "))

  #Definir quais são as notas mínimas atribuindo os valores a uma nova variável através de um
  #dicionário
    notasMinimas = {"e": cortEntrev, "t": cortTeor, "p": cortPrat, "s": cortSoft}
  #Criar uma lista para armazenar as correspondências encontradas
    candidatos_aprovados = []
  #Loop para percorrer o dicionário para localizar os valores correspondentes
    for nk, nv in notasCandidatos.items():
        correspondencia = re.match(padrao, nv)
        if correspondencia:
            e_valor = int(correspondencia.group(1)) # Obtém o valor da primeira captura (avaliação da entrevista)
            t_valor = int(correspondencia.group(2))  # Obtém o valor da segunda avaliação
            p_valor = int(correspondencia.group(3))  # Obtém o valor do teste prático
            s_valor = int(correspondencia.group(4))  # Obtém o valor das soft skills
            
            # Atribui os valores encontrados à um dicionário e esse dicionário, à uma lista
            if all(notasMinimas[key] <= value for key, value in {'e': e_valor, 't': t_valor, 'p': p_valor, 's': s_valor}.items()):
                candidatos_aprovados.append({
                    'id': nk,
                    'e_valor': e_valor,
                    't_valor': t_valor,
                    'p_valor': p_valor,
                    's_valor': s_valor
                })

    # Imprime os candidatos aprovados
    if candidatos_aprovados:
        print("Candidatos aprovados:")
        for candidato in candidatos_aprovados:
            print(f"   > Candidato {candidato['id']} <")
            print("_____Avaliações_____")
            print(f"Entrevista: {candidato['e_valor']}")
            print(f"Teste Teórico: {candidato['t_valor']}")
            print(f"Teste Prático: {candidato['p_valor']}")
            print(f"Soft Skills: {candidato['s_valor']}")
            print("*" * 30)
    # Ou imprime uma mensagem informando que nenhum candidato atendeu aos critérios de busca
    else:
        print("Nenhum candidato atendeu aos critérios de notas mínimas.")
    # Perguntar se deseja fazer uma nova busca
    continuar = input("Deseja fazer outra pesquisa (Digite 'sim' para continuar ou pressione Enter para sair)? ")
    if continuar.lower() != 'sim': #Se a resposta for diferente de "sim" o código para
        break

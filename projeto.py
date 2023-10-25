# Copyright 2023 Beatriz Miranda
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#*********************_____Código do projeto_____*******************************

#Importar as bibliotecas necessárias 
import re  #Biblioteca própria do python para definir a expressão regular
import pandas as pd #Biblioteca para fazer a exportação
#_____________________Início do código______________________
# Criar um dicionário contendo as notas geradas pelo teste fictício
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
#____________________LOOP e código principal____________________
# Criar o loop para que possa ser pesquisado quantas vezes for necessário
while True:
    # Solicitar as notas de corte para a pesquisa
    cortEntrev = int(input("Digite a nota mínima para a entrevista (e): "))
    cortTeor = int(input("Digite a nota mínima para o teste teórico (t): "))
    cortPrat = int(input("Digite a nota mínima para o teste prático (p): "))
    cortSoft = int(input("Digite a nota mínima para as soft skills (s): "))
    # Definir quais são as notas mínimas atribuindo os valores a uma nova variável através de um dicionário
    notasMinimas = {"e": cortEntrev, "t": cortTeor, "p": cortPrat, "s": cortSoft}
    # Criar uma lista para armazenar as correspondências encontradas
    candidatos_aprovados = []
    # Loop para percorrer o dicionário para localizar os valores correspondentes
    for nk, nv in notasCandidatos.items():
        correspondencia = re.match(padrao, nv)
        if correspondencia:
            e_valor = int(correspondencia.group(1))  # Obtém o valor da primeira captura (avaliação da entrevista)
            t_valor = int(correspondencia.group(2))  # Obtém o valor da segunda avaliação
            p_valor = int(correspondencia.group(3))  # Obtém o valor do teste prático
            s_valor = int(correspondencia.group(4))  # Obtém o valor das soft skills
# Atribui os valores encontrados à um dicionário e esse dicionário, à uma lista
            if all(notasMinimas[key] <= value for key, value in {'e': e_valor, 't': t_valor, 'p': p_valor, 's': s_valor}.items()):
                candidatos_aprovados.append({
                    'Candidato': nk,
                    'Entrevista': e_valor,
                    'Teste Teorico': t_valor,
                    'Teste Pratico': p_valor,
                    'Soft Skills': s_valor
                })
# Imprime os candidatos aprovados
    if candidatos_aprovados:
        print("Candidatos aprovados:")
        for candidato in candidatos_aprovados:
            print(f"   > Candidato {candidato['Candidato']} <")
            print("_____Avaliações_____")
            print(f"Entrevista: {candidato['Entrevista']}")
            print(f"Teste Teorico: {candidato['Teste Teórico']}")
            print(f"Teste Pratico: {candidato['Teste Prático']}")
            print(f"Soft Skills: {candidato['Soft Skills']}")
            print("*" * 30)
# Ou imprime uma mensagem informando que nenhum candidato atendeu aos critérios de busca
    else:
        print("Nenhum candidato atendeu aos critérios de notas mínimas.")
# Perguntar se deseja fazer outra pesquisa
    continuar = input("Deseja fazer outra pesquisa (Digite 'sim' para continuar ou pressione Enter para sair)? ")
    if continuar.lower() != 'sim':  # Se a resposta for diferente de "sim" o código para
        break
#_______________Final do LOOP / início da exportação__________________________
# Crie um DataFrame a partir da lista de dicionários dos candidatos aprovados
df = pd.DataFrame(candidatos_aprovados)
# Exporte os dados para um arquivo CSV
df.to_csv("candidatos_aprovados.csv", index=False, sep=';')

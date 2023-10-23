import re

contagem = 0

notasCandidatos = {1: "e9_t8_p7_s9",
                   2: "e8_t8_p7_s3",
                   3: "e6_t9_p9_s10",
                   4: "e7_t5_p4_s5",
                   5: "e3_t10_p10_s5",

}


# Padrão da expressão regular com X como um espaço reservado para a avaliação
padrao = r'e(\d+)_t(\d+)_p(\d+)_s(\d+)'

# Itere pelo dicionário e encontre correspondências para cada valor



cortEntrev = int(input("Digite a nota mínima para a entrevista (e): "))
cortTeor = int(input("Digite a nota mínima para o teste teórico (t): "))
cortPrat = int(input("Digite a nota mínima para o teste prático (p): "))
cortSoft = int(input("Digite a nota mínima para as soft skills (s): "))

notasMinimas = {"e": cortEntrev, "t": cortTeor, "p": cortPrat, "s": cortSoft}



while True:

    for nk, nv in notasCandidatos.items():
        correspondencia = re.match(padrao, nv)
        if correspondencia:
            e_valor = correspondencia.group(1)
            t_valor = correspondencia.group(2)
            p_valor = correspondencia.group(3)
            s_valor = correspondencia.group(4)

        candidatos_filtrados = []
        
        for nv in correspondencia.items():
            if all(candidato[key] >= nv for nk, nv in notasMinimas.items()):
                candidatos_filtrados.append(candidato)
        print(candidatos_filtrados)

    print(f" Candidato: {nk}\nAvaliações Entrevista: {e_valor};\nTeste Teorico: {t_valor};\nTeste Prático: {p_valor};\nSoft Skills: {s_valor}\n")
    
    candidatos_filtrados = buscar_candidatos(notasMinimas)


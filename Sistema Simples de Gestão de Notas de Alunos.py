def cadastrar_notas():
    notas = []
    while True:
        nota = float(input("Digite uma nota (ou -1 para encerrar): "))
        if nota == -1:
            break
        notas.append(nota)
    return notas

def calcular_media(notas):
    if len(notas) > 0:
        return sum(notas) / len(notas)
    else:
        return 0

def determinar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def relatorio_final(notas, media, situacao):
    print("\nRelatório Final")
    print("Notas:", notas)
    print("Média:", round(media, 2))
    print("Situação do Aluno:", situacao)

# Programa Principal
notas = cadastrar_notas()
media = calcular_media(notas)
situacao = determinar_situacao(media)
relatorio_final(notas, media, situacao)

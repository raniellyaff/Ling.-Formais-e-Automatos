## ATIVIDADE 3 - LINGUAGENS FORMAIS E AUTÔMATOS ##

estados = input().split()
inicial = input().strip()
aceitacao = input().split()
alfabeto = input().split()

#constrói tabela de transição
transicao = {}
for estado in estados:
    transicao[estado] = {}

#para cada estado, lê uma linha com o estado e seus próximos estados
for i in range(len(estados)):
    linha = input().split()
    estado_origem = linha[0]
    proximos_estados = linha[1:]
    
    #usa só as primeiras colunas correspondentes ao alfabeto
    for j, simbolo in enumerate(alfabeto):
        transicao[estado_origem][simbolo] = proximos_estados[j]

#lê as cadeias de entrada
cadeias = input().split()

#verifica cada cadeia
for cadeia in cadeias:
    atual = inicial
    
    #verifica se a cadeia é vazia, caso o estado inicial seja de aceitação
    if cadeia == 'vazia' and atual in aceitacao:
        print("aceita")
        continue
    elif cadeia == 'vazia' and atual not in aceitacao:
        print("rejeita")
        continue

    valida = True
    for c in cadeia:
        if c not in alfabeto:
            valida = False
            break
        if atual in transicao and c in transicao[atual]:
            atual = transicao[atual][c]
        else:
            valida = False #caso a transição não exista
            break
    
    if not valida:
        print("rejeita")
    elif atual in aceitacao:
        print("aceita")
    else:
        print("rejeita")
## ATIVIDADE 1 - LINGUAGENS FORMAIS E AUTÔMATOS ##
estados = ["q1", "q2", "q3"] #lista com os estados    
inicial = "q1" #estado inicial
aceitacao = ["q2"] #lista com os estados que aceitamos                
alfabeto = ["0", "1"] #a maquina so reconhece 0 e 1, então essa será o nosso alfabeto 

transicao = {                     
    "q1": {"0": "q1", "1": "q2"}, #se em q1 estiver '0' vai para q1, se estiver '1' vai para q2
    "q2": {"0": "q3", "1": "q2"}, #se em q2 estiver '0' vai para q3, se estiver '1' continua em q2
    "q3": {"0": "q2", "1": "q2"} #se em q3 estiver '0' vai para q2, se estiver '1' também vai para q2
}

cadeias = input("").split() #divide a string digitada em mais partes (nos casos de espaços)

for cadeia in cadeias: #percorre as cadeias de entrada
    atual = inicial #o estado inicial será o atual                      
    for c in cadeia: #percorre cada simbolo da cadeia
        if c not in alfabeto: # caso não encontre um simvolo que etsa no alfabeto
            atual = None #nao executa
            break #para de rodar
        atual = transicao[atual][c] #caso contrário consulta o dicionário de transição e move para o próximo estado

    if atual in aceitacao: #verifica se o estado final é de aceito
        print("aceita")
    else:
        print("rejeita") #se não for a cadeia é rejeitada


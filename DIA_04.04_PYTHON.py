## Aprendendo lista.

# Iniciando a lista
lista=[]

# Adiciona items NO FIM da lista
lista.append(1)
lista.append(2)
lista.append(5)
lista.append(5)
lista.append(7)

# Adiciona items na posição que você desejar
    # Aqui vamos inserir na terceira posição
lista.insert(2,9)

# Printa a lista inteira
print(f'A lista inteira é: ',lista)

print(f'O primeiro item da lista é:',lista[0])

# Um método de escolher o item começando pelo final, muito útil!
print(f'O ultimo item da lista é:',lista[-1])

# Para inserir varios valores de uma forma diferente
    # No começo
lista=lista+[1,2,3]
    # No final
lista=[3,2,1]+lista

print(f'Fatia inteira atualmente é:',lista[:])

# A fatia [x:y] do python é [inclusiva:exclusiva]
fatia=lista[0:1]
print(f'Como a fatia [x:y] em python é incl:excl, nossa fatia é apenas o número',fatia)
fatia=lista[0:2]
print(f'Agora a fatia tem dois números:',fatia)

# Esse comando vai remover o PRIMEIRO número 1 da lista (não o valor na posição 1)
lista.remove(1)

print(f'Lista inteira após um único remove(1):',lista[:])

# Se você quiser remover todos os números 1 da lista, use um while
while(1 in lista):
    lista.remove(1)

print(f'Lista inteira após o while de remove(1):',lista[:])

# Se você quiser remover um valor e muma posição especifica
lista.pop(5)
print(f'Lista inteira após o pop[5]:',lista[:])

# Se você escrever isso aqui:
lista.pop()
# Ele vai remover o primeiro valor

# Se você quiser salvar o valor removido, você pode salvar como uma lista
removidos = []
removidos = lista.pop(0)
print(f'O valor removido foi o primeiro valor da lista, o número',removidos)



classe = [
    ["A", "Rodrigo", [1,2,3,4,5,6,7]], # 0
    ["B", "Ranma", [8,9,10,11,12,13,14]], # 1
    ["C", "Caroline", [15,16,17,18,19,20,21]], # 2
    ["D", "Nebulonix", [1,2,3,4,5,6,7,8,9,10]], # 3
    ["E", "Lenca", [1,2,3,4,5,6,7,8,9,10]], # 4
    ["F", "Archzinho", [1,2,3,4,5,6,7,8,9,10]] # 5
]

print("\n"*10)
print(f'Meu nome é',classe[0][1][:])
print(f'Eu tenho um amigo incrível chamado',classe[1][1][:])
print(f'E me inspiro muito na',classe[2][1][:])
print(f'O {classe[3][1][0:4]} é um amigo nota {classe[3][2][-1]}')
print(f'{classe[4][0][:]}u adoro ver a minha amiga {classe[4][1][:]} estudar!')
print(f'Eu conheço o {classe[5][1][0:4]} a muito tempo e a presença dele é muito confortante!')
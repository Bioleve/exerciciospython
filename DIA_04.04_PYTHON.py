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

# Se você quiser salvar o valor removido, você pode salvar como uma variável
primeiroValor = lista.pop(0)
print(f'O valor removido foi o primeiro valor da lista, o número',primeiroValor)

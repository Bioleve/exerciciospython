## Aprendendo lista.

# Iniciando a lista
lista=[]

# Adiciona items NO FIM da lista
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


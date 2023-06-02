lista = ['mãe', 35, 'pai', 38, 'danda', 18, 'lele', 3, 'ago', 16, 'ropa', 11, 'teca', 5]
print(lista)
print(len(lista))       #quantidade de itens na lista

print(type(lista))          #tipo da lista

print(type(lista[1]))           #tipo do item da lista no index tal

lista2 = list(('raquel', 'sinval', 'dandara', 'elena', 'ariel', 'mocinha', 'teca'))
print(lista2)
print(type(lista2))

lista.extend(lista2)        #junção da lista1 com lista2
print(lista)

lista2.append('FAMÍLIA')        #adiciona item no fim da lista
print(lista2)

lista.insert(3, 'pessoas')          #adiciona item em index específico
print(lista)

lista.remove('pessoas')      #remove item da lista
print(lista)

lista2.clear()                #apaga os items da lista
print(lista2)

print(lista.index('danda'))         #printa o número do index do item
print(lista.count('danda'))             #quantidade de items com aquele nome

lista2.sort()            #sorteia a lista de trás pra frente e vice-versa
print(lista2)

lista2.reverse()            #coloca a lista ao contrário ****
print(lista2)

lista3 = lista.copy()           #copia o conteúdo de uma lista para outra lista, ou método? **
print(lista3)

lista.pop()             #remove o último item da lista   #lista.pop(1) remove por index
print(lista)

del lista2[5]               #outro jeito de remover item por index
print(lista2)

del lista                       #deleta a lista toda

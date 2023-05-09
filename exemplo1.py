notas = []

opcao = -1
while opcao!=3:
    print("1- Informar notas \n 2- Exibir notas \n 3- Calcular média \n 4- Sair")
    opcao=int(input("Escolha sua opção:"))
    if opcao==1:
        #pedindo ao usuário a nota para assim colocar dentro da lista
        notas.append(float(input("Digite a nota aqui:")))
    elif opcao==2:
        for x in notas:
            print(notas)
    elif opcao==3:
        #sum faz a soma das notas e len pega o total de itens da lista
        print(sum(notas)/len(notas))

perguntas = []            #lista vazia para inserção de valores
perguntas.append(input("Telefonou para a vítima?"))   #append adiciona valores no final da lista!

perguntas.append(input("Esteve no local do crime?"))

perguntas.append(input("Mora perto da vítima?"))

perguntas.append(input("Devia para a vítima?"))

perguntas.append(input("Já trabalhou com a vítima?"))

for iten in perguntas:
    print(iten)       #aqui o for circula pelos itens, um por um

if perguntas.count("sim") == 2:
    print("Você é suspeito.")
elif perguntas.count("sim") >= 3 and perguntas.count("sim")<= 4:
    print("Você é cúmplice.")
elif perguntas.count("sim") == 5:
    print("Você é o assassino(a).")
else:
    print("Você é inocente.")

print(perguntas[3])     #com o método append conseguimos acessar os índices da lista sem problemas

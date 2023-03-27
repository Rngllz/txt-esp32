

with open("txt/teste.txt", "r", encoding="utf-8") as arquivo:
    linha = arquivo.readlines()
    print(linha)
    print(linha[0])
    print(len(linha[0]))


with open("txt/aalala.txt", "w", encoding="utf-8") as arquivo:
   
    for num in range(len(linha)):

        if '"' in linha[num]:
            sentença = linha[num]
            linha[num] = sentença.replace('"','/')

        if (linha[num].find('\n') == len(linha[num])-1):
            espaço = linha[num]
            print("espaço")
            linha[num] = espaço.replace('\n','')

        linha_formatada = '("' + linha[num] + '"@\n'
        linha[num] = linha_formatada

        arquivo.write(linha[num])
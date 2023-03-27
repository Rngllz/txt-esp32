

with open("txt/teste.txt", "r", encoding="utf-8") as arquivo:
    linha = arquivo.readlines()
    # Pega todas as linhas e coloca em uma lista

with open("txt/aalala.txt", "w", encoding="utf-8") as arquivo:
   
    for num in range(len(linha)):

        # Condição para as aspas no código
        if '"' in linha[num]:
            linha[num] = linha[num].replace('"','\\"')

        # Condição preparatória para a formatar a linha:
        #
        #       Em uma lista todas as partes que possuem
        #       uma quebra de linha são salvas com um "\n"
        #       e isso estraga a formatação quando tento
        #       adicionar algo no final da frase. Por isso  
        #       existe está condição, ela retira o \n que 
        #       logo após já é recolocado.
        #
        if (linha[num].find('\n') == len(linha[num])-1):
            linha[num] = linha[num].replace('\n','')

        # Adiciona as partes frontais e posteriores,
        # junto com a quebra de linha "\n".
        linha[num] = 'client.println("' + linha[num] + '");\n'

        arquivo.write(linha[num])
        # Lança a linha para o novo arquivo,
        # repete este processo em todas as linhas.
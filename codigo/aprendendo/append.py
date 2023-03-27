
#          Adiciona uma nova linha para o arquivo.
#          Padrão = concatena a linha já existente e a nova
with open("local_do_arquivo/arquivo.txt","a") as arquivo:
    arquivo.write("\nnova info a ser adicionada")
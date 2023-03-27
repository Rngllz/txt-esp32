
#                                          r = READ (LER)
#                                          w = WRITE (ESCREVER)
#                                          a = APPEND (ADICIONAR)
with open("local_do_arquivo/arquivo.txt", "r", encoding="utf-8") as arquivo:

    email = arquivo.read()
    print(email) #  read() é para arquivos pequenos, uma linha; email, senhas, códigos, etc

#                                                       para ler arquivos em potugu~ês
with open("local_do_arquivo/arquivo.txt", "r", encoding="utf-8") as arquivo:
    
    mensagem = arquivo.readlines()
    print(mensagem)# transforma o texto em uma lista, com suas linhas e quebras de linhas



for linha in mensagem:
    if "faturamento" in linha:
        print(linha) # imprime linhas unicas de acordo com suas condições

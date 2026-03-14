# Eliabe e Ivo Junior
contador = 0

def incrementar_contador():
    global contador
    mensagem = ''
    contador += 1
    print(f'Contador: {contador}')

incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()

print(f'Mensagem: {mensagem}') # 'mensagem' não está definida, isso causará um erro.
while True:
    numero_1= input("digite um numero: ")
    numero_2=input("digite outro numero: ")
    operador= input("digite um operador: (+-*/): ")
    numeros_validos = None
    sair= ""
    try:
        num_1_float= float(numero_1)
        num_2_float= float(numero_2)
        numeros_validos= True
    except:
        numeros_validos=None
    if numeros_validos is None:
        print("um ou ambos os numeros digitados sao invalidos.")
        continue
    operadores_permitidos= ("+-*/")
    if operador not in operadores_permitidos:
        print("digite um operador valido")
        continue
    if len(operador)>1:
        print("voce digitou mais de um operador")
        continue
    if operador == "+":
        print ("o resultado é ",num_1_float + num_2_float)
    elif operador== "-":
        print("o resultado é ", num_1_float - num_2_float)
    elif operador== "/":
        print("o resultado é ",num_1_float / num_2_float)
    elif operador== "*":
        print("o resultado é ", num_1_float * num_2_float)
    sair= input("Deseja sair [S]im ou [N]ão: ").lower().startswith("s")
    if sair is True:
        break
    else:
        continue
import string 

def limpar_cpf(cpf):
    return "".join(filter(str.isdigit, cpf))

def calcular_digito_verificador(cpf_cortado):
    cpf_validador = 0
    contador = 2
    for i in reversed(cpf_cortado):
        cpf_validador += int(i) * contador
        contador +=1
    cpf_validador %= 11
    if cpf_validador < 2:
        digito_verificador = 0
    else:
        digito_verificador = 11 - cpf_validador
    return digito_verificador

def validar_cpf(cpf):
    cpf_limpo = limpar_cpf(cpf)
    cpf_cortado = cpf_limpo[:9]
    print(cpf_limpo)
    digito_verificador1 = calcular_digito_verificador(cpf_cortado)
    cpf_cortado += str(digito_verificador1)
    digito_verificador2 = calcular_digito_verificador(cpf_cortado)
    cpf_cortado += str(digito_verificador2)
    print(cpf_cortado)
    return cpf_limpo == cpf_cortado

cpf_inserido = input("Insira o CPF para validar: ")
valido = validar_cpf(cpf_inserido)
print(valido)
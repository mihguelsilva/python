# FUNCOES

# calcular area do retangulo
def area_retangulo(base,altura):
    area = float(base) * float(altura)
    print(f"A área do retângulo é {area} de comprimento")

# calcular area do circulo
def area_circulo(raio):
    pi = 3.141592
    area = pi * float(raio) ** 2
    print(f"A área do circulo é {area} de comprimento")

# calcular desconto de preco
def calcular_desconto(preco, desconto):
    porcentagem = float(preco) * float(desconto) / 100
    valor_final = float(preco) - float(porcentagem)
    print(f"O valor do produto sem desconto é R${preco} e com desconto R${valor_final}")

# converter real para dolar
def conv_real_dolar(real, k):
    calculo = float(real)/k
    print(f"O resultado da conversão de real para dólar é ${calculo}")

# converter dolar para real
def conv_dolar_real(dolar, k):
    calculo = float(dolar) * k
    print(f"O resultado da conversão de dólar para real é R${calculo}")

# operacoes para verificar o que usuario deseja realizar
def calcular(operacao):
    if operacao == "1":
        base = input("Informe o tamanho da base do retângulo: ")
        altura = input("Informe o tamanho da altura do retângulo: ")
        area_retangulo(base, altura)
    elif operacao == "2":
        raio = input("Informe o raio do circulo: ")
        area_circulo(raio)
    elif operacao == "3":
        preco = input("Informe o preco do seu produto: ")
        desconto = input("Informe quantos por cento de desconto terá seu produto: ")
        calcular_desconto(preco, desconto)
    elif operacao == "4":
        real = input("Quantos reais você deseja converter em dólar? ")
        conv_real_dolar(real, 5.20)
    elif operacao == "5":
        dolar = input("Quantos dólares você deseja converter em reais? ")
        conv_dolar_real(dolar, 5.20)

# questionando ao usuario o que deve ser feito
def pergunta(callback):
    
    # variavel com string em bloco para facilitar formatacao
    operacao = input("""O que você deseja calcular? [Escolha o número da operação]
1 (Área do Retângulo)
2 (Área do Círculo)
3 (Calcular desconto)
4 (Converter real para dólar)
5 (Converter dólar para real)""")
    
    callback(operacao)

# executando funcao com uma callback
pergunta(calcular)
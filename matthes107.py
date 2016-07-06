while True:
    try:
        num1 = int(input("Escreva um número: "))
        
    except ValueError:
        print("Digite um valor numerico")
        num1 = int(input("Escreva um número: "))
    
    try:
        num2 = int(input("Escreva um número: "))
        
    except ValueError:
        print("Digite um valor numerico")
        num2 = int(input("Escreva um número: "))

soma = num1+num2

print("A soma dos dois números: ", soma)
def multiplo():
    try:
        number1 = int(input('Insira o início: '))
        number2 = int(input('Insira o último número: '))

        multiplos_3 = []
        multiplos_5 = []

        for i in range(number1, number2):
            if i % 3 == 0 and i % 5 == 0:
                print("fizzbuzz")
            elif i % 3 == 0:
                multiplos_3.append(i)
                print("fizz")
            elif i % 5 == 0:
                multiplos_5.append(i)
                print("buzz")
        
        print("Múltiplos de 3:", multiplos_3)
        print("Múltiplos de 5:", multiplos_5)

    except ValueError:
        print("Por favor, insira apenas números inteiros.")

multiplo()

def gravar_nota():
    while True:
        try:
            nota = float(input("Insira a nota do aluno: "))
            if nota >= 0.0 and nota <= 10.0:
                print(nota)
                break
            else:
                print("Valor inválido.")
        except ValueError:
                print("Valor inválido.")
gravar_nota()
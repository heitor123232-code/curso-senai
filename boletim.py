def ler_nota(rotulo: str) -> float:
    while True:
        texto = input(f"{rotulo}: ").strip().replace(",", ".")
        try:
            nota = float(texto)
            if 0 <= nota <= 10:
                return nota
            print("Digite uma nota entre 0 e 10.")

        except ValueError:
            print("Digite um número válido.")

print("=== Boletim simples ===")
nome = input("Digite seu nome: ")
nota1 = ler_nota("Nota 1")
nota2 = ler_nota("Nota 2")
nota3 = ler_nota("Nota 3")

media = (nota1 + nota2 + nota3) / 3

print(f"Média das notas: {media:.2f}")
if media >= 6:
    print(f"Olá {nome}, você foi Aprovado!")
else:
    print(f"Olá {nome}, você foi Reprovado!")
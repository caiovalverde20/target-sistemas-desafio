def reverse_string(s):
    inversa = ""
    for char in s:
        inversa = char + inversa
    return inversa


texto = input("Digite uma string: ")
print(f"String invertida: {reverse_string(texto)}")

nota1 = int(input())
media = int(input())
nota2 = 2 * media - nota1
if 0 < nota1 <= 100 and 0 < media <= 100 and 0 < nota2 <= 100:
    print(nota2) 
else:
    print("Nota ou média abaixo de 0 ou acima de 100")

#Por quê o if ternario não funciona?
# print(nota2) if 0 < nota1, media, nota2 <= 100 else print("Impossível pois a nota ou média está abaixo de 0 ou acima de 100")


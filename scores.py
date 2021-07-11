def scores(a, b):
    print("nota inválida") if a < 0 or b < 0 or a > 10 or b > 10 else print((a+b)/2)

scores(float(int(input())), float(int(input())))
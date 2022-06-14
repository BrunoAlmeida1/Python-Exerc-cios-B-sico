# Programa que imprimi números nesse formato:
# 1
# 1 2
# 1 2 3

def imprimi(n):
    x = 1
    while x <= n:
        for p in range(x):
            print(p+1, end=" ")
        x += 1
        print("\n")


print("~"*50)
num = int(input("Digite um número: "))
print("\n")
imprimi(num)
print("\n")
print("~"*50)

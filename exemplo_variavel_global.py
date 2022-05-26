from re import X


def mudar():
    global x
    x -= 1

x = 10

mudar()

print(x)
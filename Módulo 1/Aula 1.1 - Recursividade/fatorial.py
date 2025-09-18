def fatorial(n):
    if (n == 0):
        return 1
    else:
        print(f'{n} * {n-1}!')
        return n * fatorial(n-1)

print(f'O fatorial de {4} é {fatorial(4)}')
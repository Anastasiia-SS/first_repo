pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool / quantity
    chunk = int(chunk)
    print(f'Each person gets {chunk} units of currency.')
except ZeroDivisionError:
    print('Divide by zero completed!')


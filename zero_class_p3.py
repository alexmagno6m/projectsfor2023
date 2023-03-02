# for looping on various iterables
# same size, not unpacking items on variables
s = [(1, 2, 3), (4, 5, 6)]
for item in s:
    print(item)

# same size, unpacking items on individuals variables
s = [(1, 2, 3), (4, 5, 6)]
for x, y, z in s:
    print(x, y, z)
print('is', x)

# different size, unpacking items
s = [(1, 2), (3, 4, 5), (6, 7, 8, 9)]
for x, y, *extra in s:
    print(x, y, *extra)
print('is', extra)
# Los valores almacenados en la variable extra se colocan en una lista

s = [1, 2, 3]
t = [4, 5, 6]
for x, y in zip(s, t):
    z = (x, y)
    print(z)

i = 0
while i < len(s):
    print(i)
    i += 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
while i < len(numbers):
    print(f'la potencia de {numbers[i]} es {numbers[i]**2}')
    i += 1
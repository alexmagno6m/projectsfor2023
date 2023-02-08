# break statement
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

print('done')

# continue statement
x = 0
while x < 10:
    x += 1
    if x == 5:
        print('x is 5')
        continue
    print(x)

print('done')

# Triple-qouted
print('''Content-type: text/html
<h1> Hello World </h1>
Click <a href="http://www.python.org">here</a>.
''')

# Format
year = 2023
print(f'current year is {year:>3d}')
print('current year is {}'.format(year))

# Slicing
a = 'Hello world'
print(len(a))

b = a[4]
print(b)

c = a[-1]
print(c)

d = a[:5]
print('is', d)

e = a[6:]
print(e)

f = a[3:8]
print(f)

g = a[:-5]
print(g)

# replace
h = a.replace('Hello', 'Cruel')
print(h)

# split
string = 'zen of python'
s1 = string.split(' ')
print(s1)



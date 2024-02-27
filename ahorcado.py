word = "juego"
print("_ "*len(word))
print(word.find('r'))

string = "hola mundo"

positions = []

for i in range(len(string)):
  if string[i] == "o":
    positions.append(i)

print(positions)
result=''
letter = 'o'
for i in range(len(string)):
    if i in positions:
        result = result + letter
    else:
        result = result + "_"

print(result)

numbercard = '43423'
print(numbercard.find('4'))

word = 'Afg12'
print(any(word.isupper() for c in word))

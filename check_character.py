string = "hola"
index = 0
while True:
        if string[index].isdecimal():
            print('checked')
            break
        else:
            index += 1
            if index == len(string) - 1:
                print('no decimal')
                break
'''
for x in string:
    if x.isdigit():
        print("checked")

print(string.find('h'))
'''
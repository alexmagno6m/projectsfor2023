# Lists
names = ['Dave', 'Paula', 'Thomas', 'Lewis']

# insert method
names.insert(2, 'Andrea')
print(names)

# create list
names_2 = []
names_3 = list('Alexander')
print(names_3)

# sets
brands = ['apple', 'samsung', 'huawei', 'hp', 'apple']
brands2 = set(brands)
print(brands2)

brands3 = {'apple', 'samsung', 'huawei', 'hp'}

brands4 = {'apple', 'xiaomi', 'google', 'lenovo'}
a = brands3 | brands4
print(a)
b = brands3 & brands4
print(b)
c = brands3 - brands4
print(c)
d = brands4 - brands3
print(d)
e = brands4 ^ brands3
print(e)

# adding element to set
brands4.add('motorola')
print(brands4)

# adding multiple elements use update({new_item1, new_item2})
# remove element, o raise error
brands4.remove('motorola')
print(brands4)
# discard, similar to remove, but check if index exist, doesn’t raise an exception if the item isn’t present.
brands4.discard('nokia')
print(brands4)
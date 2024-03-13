# Lists
names = ['Dave', 'Paula', 'Thomas', 'Lewis']

# insert method
names.insert(2, 'Andrea')
print(names)

# count elements
print(names.count('Andrea'))

# extend elements
names2 = ['Pedro', 'Juan']
names.extend(names2)
print(names)

# index return
print(names.index('Pedro'))

# pop elements, deleted by index, pedro deleted
names.pop(5)
print('pop', names)

# remove lists, deleted by item name
names.remove('Juan')
print('remove', names)

# sort, orders elements, descending reverse
names.sort()
print('order', names)
names.sort(reverse=True)
print('descending', names)

# reverse object by index
names.reverse()
print('reverse', names)

# max, min operate on numbers items
numbers = [5, 20, 100, 45, 0]
print(max(numbers))
print(min(numbers))

# create list
names_2 = []
names_3 = list('Alexander')
print(names_3)

# sets
brands = ['apple', 'samsung', 'huawei', 'hp', 'apple']
brands2 = set(brands)
print('brands2', brands2)

brands3 = {'apple', 'samsung', 'huawei', 'hp'}

brands4 = {'apple', 'xiaomi', 'google', 'lenovo'}
# union
a = brands3 | brands4
a1 = brands3.union(brands4)
print('union', a, a1)

# intersection
b = brands3 & brands4
b1 = brands3.intersection(brands4)
print('intersection', b, '-', b1)

# difference
c = brands3 - brands4
c1 = brands3.difference(brands4)
print('difference', c, c1)

# difference
d = brands4 - brands3
d1 = brands4.difference(brands3)
print('difference', d, '-', d1)

# symmetric difference
e = brands4 ^ brands3
e1 = brands3.symmetric_difference(brands4)
print('symetric', e, '-', e1)

# adding element to set
brands4.add('motorola')
print(brands4)

# adding multiple elements use update({new_item1, new_item2})
# remove element, o raise error
brands4.update({'alcatel', 'poco phone'})
print('update', brands4)

brands4.remove('motorola')
print(brands4)
# discard, similar to remove, but check if index exist, doesn’t raise an exception if the item isn’t present.
brands4.discard('nokia')
print(brands4)
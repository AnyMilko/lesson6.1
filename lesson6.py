my_dict = {'Marina': 1999, 'Yana': 2000, 'Jana': 1997}
print(my_dict)
my_dict['Ann'] = 1998
print(my_dict)
print(my_dict['Marina'])
my_dict['Lena'] = 2005
print(my_dict)
my_dict.update({'Sasha':1999,
                'Lyiza':2005})
print(my_dict)
a = my_dict.pop('Lena')
print(my_dict)
print(a)

my_set = {1, 2, 3, 1, 2, 3, 4, 'pen', True, (1,2,3)}
print(my_set)
print(my_set.add(8))
print(my_set.add(9))
print(my_set)
print(my_set.discard(1))
print(my_set)

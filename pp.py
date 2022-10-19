# list comprehension

from re import X


lis = [('name', 66), ('raj',45), ('josh', 23)]

res = [x for name,age in lis if x == 'josh']

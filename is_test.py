list_a = [10,20,30]
list_b = [10, 20, 30]

if list_a == list_b:
    print('list_a is list_b')
else:
    print('list_a is not list_b')

print(id(list_a))
print('list_a는 {}'.format(id(list_a)))
print('list_b는 {}'.format(id(list_b)))
print(id(list_b))
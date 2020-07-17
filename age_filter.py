def adult_func(n):
    if n>=19:
        return True
    else:
        return False

print(adult_func(18))

ages = [34,23,12,15,35]
print('성년리스트')

for a in filter(adult_func , ages):
    print(a)
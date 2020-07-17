ages = [34,23,12,15,35]
print('성년리스트')

for a in filter(lambda x: x>=19 , ages):
    print(a)
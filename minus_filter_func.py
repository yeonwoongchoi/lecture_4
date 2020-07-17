# n_list = [1,20,-3,4,20,-20,100]
# print('마이너스 리스트')

# for a in filter(lambda x : x<0 ,n_list):
#     print(a)



###OR
n_list = [1,20,-3,4,20,-20,100]

minus_arr = []

for a in filter(lambda x: x<0 , n_list):
    minus_arr.append(a)

print(minus_arr)
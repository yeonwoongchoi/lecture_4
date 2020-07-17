# class Circle:
#     def __init__(self, name, radius, PI):
#         self.name = name
#         self.radius = radius
#         self.PI =PI


#     def area(self):
#         return self.PI * self.radius ** 2
        
# c1 = Circle("c1", 4, 3.14)
# print("c1의 면적:", c1.area())
# c2 = Circle("c2", 6, 3.141)  
# print("c2의 면적:", c2.area())
# c3 = Circle("c3", 5, 3.1415)
# print("c3의 면적:", c3.area())



class Vector3D:
    def _init_(self,x,y,z): # 변수 x,y,z
        self.x=x 
        self.y=y #생성자 만들기
        self.z=z
    def _str_(self): #문자열로 출력하려면 사용, 반환 어떻게 하는 지 만든 것
        return '({},{},{})'.format(self.x, self.y, self.z)
    def _eq_(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return 'Vectors are identical'
        else :
            return 'Vectors are different'
v1=Vector3D(1,2,3)
v2=Vector3D(1,2,4)
print(v1==v2)
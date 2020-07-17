class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y #self.__y라고 한다면 밖에서 못써먹는 변수로 변한다.

    def eq(self , other): #str은 문자열 출력하려고 썼다.
        return self.x == other.x and self.y == other.y    

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector2D(10,20)
v2 = Vector2D(20,30)
v3 = v1.eq(v2)
print(v3)
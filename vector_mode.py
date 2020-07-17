class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y #self.__y라고 한다면 밖에서 못써먹는 변수로 변한다.

    def __str__(self): #str은 문자열 출력하려고 썼다.
        return '({} , {})'.format(self.x , self.y)    
    
    def __mod__(self, other):
        return Vector2D(self.x %other.x , self.y %other.y)


v1 = Vector2D(10,20)
v2 = Vector2D(20,30)
v3 = v2%v1
print(v3)
##add.py에서 +를 mode, %로 바꿔서 만든다.

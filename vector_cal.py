class Vector2D:


    def __str__(self): #str은 문자열 출력하려고 썼다.
        return '({} , {})'.format(self.x , self.y)    


    def __init__(self, x, y):
        self.x = x
        self.y = y #self.__y라고 한다면 밖에서 못써먹는 변수로 변한다.


    def eq(self , other): #str은 문자열 출력하려고 썼다.
        return self.x == other.x and self.y == other.y    

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def add(self, other):
        return Vector2D(self.x +other.x , self.y +other.y)

    def __add__(self, other):
        return Vector2D(self.x +other.x , self.y +other.y)


    def sub(self, other):
        return Vector2D(self.x - other.x ,self.y - other.y )
        ## def__떙땡__과 def 땡땡의 차이
    def __sub__(self, other):
        return Vector2D(self.x - other.x ,self.y - other.y )


    def __mod__(self, other):
        return Vector2D(self.x %other.x , self.y %other.y)



    def __del__(self):
        print("This process is End!")
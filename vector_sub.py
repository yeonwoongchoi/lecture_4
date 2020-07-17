class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return '({} , {}, {})'.format(self.x , self.y , self.z)

    def sub(self, other):
        return Vector3D(self.x - other.x ,self.y - other.y ,self.z - other.z  )
        ## def__떙땡__과 def 땡땡의 차이
    def __sub__(self, other):
        return Vector3D(self.x - other.x ,self.y - other.y ,self.z - other.z  )
v1 = Vector3D(10,20,30)
v2 = Vector3D(20,30,40)
# v3 = v1.sub(v2)
v4 = v1-v2
print(v4)
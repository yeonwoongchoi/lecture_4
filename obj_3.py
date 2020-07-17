class Cat:
    color = 'red'
    sound = '야옹야옹'
        #생성자 메소드
    def __init__(self , name , color, sound):
        self.name = name
        self.color = color
    def meow(self,name,sound):
        print("길냥이 {} 이는 색깔이 {}구요 자주 야옹~! 야옹~! 거려요".format(self.name, self.color))
        print('못생긴 {}'.format(self.name, self.color, self.sound,self.sound ))

gang_cat = Cat('미옹', '컬러풀', "미야옹")
# jong_cat = Cat('태경', '똥이')
gang_cat.meow('라온', '야옹야옹')
# jong_cat.meow('라온')
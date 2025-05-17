#2차원 화면에 있는 직사각형의 둘레와 넓이 구하기

class Point:
    def __init__(self, x=0, y=0):  # 기본값 (0, 0)
        self.__x = x
        self.__y = y

    def show(self):
        print(f'({self.__x}, {self.__y})')

    def set(self, x, y):
        self.__x = x
        self.__y = y

    def get(self):
        return (self.__x, self.__y)
    

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__lt = Point(x1, y1)
        self.__rb = Point(x2, y2)

    def show(self):
        lt_x, lt_y = self.__lt.get()
        rb_x, rb_y = self.__rb.get()
        print(f"현재 사각형의 좌측 상단과 우측 하단 꼭짓점: ({lt_x}, {lt_y})({rb_x}, {rb_y})")

    def getWidth(self):
        rb_x, rb_y = self.__rb.get()
        lt_x, lt_y = self.__lt.get()
        return  rb_x - lt_x
    
    def getHeight(self):
        rb_x, rb_y = self.__rb.get()
        lt_x, lt_y = self.__lt.get()
        return rb_y - lt_x
    
    def getArea(self):
        return self.getWidth()*self.getHeight()
    
    def getPerimeter(self):
        return 2 * (self.getHeight() + self.getWidth())



#주프로그램부
if __name__ == '__main__':
    r1 = Rectangle(5, 5, 20, 10)
    a = r1.getArea()
    p = r1.getPerimeter()

    r1.show()
    print(f'\n넓이는 {a}, 둘레는 {p}')

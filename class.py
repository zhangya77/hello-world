
class Rectangle:
    def __init__(self, length, weight):
        if (length <= 0 or weight <= 0):
            raise ValueError("length and weight must be greater than 0")
        self.l = length
        self.w = weight
    @property
    def area(self):
        return self.l * self.w

    @property
    def perimeter(self):
        return 2 * (self.w + self.l)

    def __str__(self):
        return'Rectangle (l=%d,w=%d)' % (self.w, self.l)
class Square(Rectangle):
    def __init__(self,side):
        if (side <= 0):
            raise ValueError("side length must be greater than 0")
        super().__init__(side, side)

# 在类外部实例化和使用
rt = Rectangle(3, 4)
print(rt.area)  # 输出: 12
print(rt.w)
print(rt.perimeter)
print(rt)

sq = Square(5)
print(sq.w)
print(sq.l)
print(sq.area)
print(sq.perimeter)
print(sq)

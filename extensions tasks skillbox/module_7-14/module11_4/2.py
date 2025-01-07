class Point:
    count_points = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.count_points += 1
        print(f'Инициализировалась точка с координатами: х = {self.x} и y = {self.y}')

    def info_points(self):
        print(self.count_points)


first_point = Point(5, 4)
second_point = Point(2, 1)
print(Point.count_points)

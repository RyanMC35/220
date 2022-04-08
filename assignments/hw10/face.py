from graphics import Circle, Line, Polygon, Point


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        center = self.head.getCenter()
        radius = self.head.getRadius()
        point_3 = center.clone()
        point_3.move(0, (radius / 1.5))
        point_1 = self.mouth.getP1()
        point_2 = self.mouth.getP2()
        self.mouth = Polygon(point_1, point_2, point_3)
        self.mouth.draw(self.window)

    def shock(self):
        point_1 = self.mouth.getP1()
        point_2 = self.mouth.getP2()
        radius = (point_1.getX() - point_2.getX()) / 2
        center = Point((point_1.getX() - radius), point_1.getY())
        circle = Circle(center, radius / 2)
        self.mouth.undraw()
        self.mouth = circle
        self.mouth.draw(self.window)

    def wink(self):
        center = self.left_eye.getCenter()
        radius = self.left_eye.getRadius()
        point_1 = center.clone()
        point_1.move(radius, 0)
        point_2 = center.clone()
        point_2.move(-radius, 0)
        self.left_eye.undraw()
        self.left_eye = Line(point_1, point_2)
        self.smile()
        self.left_eye.draw(self.window)





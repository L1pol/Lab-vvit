class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius

circle = Circle(20)
print(f"Начальный радиус: {circle.get_radius()}")
circle.set_radius(50)
print(f"Новый радиус: {circle.get_radius()}")
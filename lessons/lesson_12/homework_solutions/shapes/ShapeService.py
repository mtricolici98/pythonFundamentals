from lessons.lesson_12.homework_solutions.shapes.Circle import Circle
from lessons.lesson_12.homework_solutions.shapes.Rectangle import Rectangle
from lessons.lesson_12.homework_solutions.shapes.Square import Square


class ShapeService:
    DEFAULT_INNER_COLOR = 'white'
    DEFAULT_OUTER_COLOR = 'black'

    @staticmethod
    def create_default_circle(radius):
        return Circle(radius, inner_color=ShapeService.DEFAULT_INNER_COLOR,
                      border_color=ShapeService.DEFAULT_OUTER_COLOR)

    @staticmethod
    def create_default_square(side_length):
        return Square(side_length, inner_color=ShapeService.DEFAULT_INNER_COLOR,
                      border_color=ShapeService.DEFAULT_OUTER_COLOR)

    @staticmethod
    def create_default_rectangle(width, length):
        return Rectangle(width, length, inner_color=ShapeService.DEFAULT_INNER_COLOR,
                         border_color=ShapeService.DEFAULT_OUTER_COLOR)

    @staticmethod
    def color_shapes(shapes, color_inner, color_outer):
        for shape in shapes:
            shape.set_inner_color(color_inner)
            shape.set_border_color(color_outer)

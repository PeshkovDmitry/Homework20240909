import doctest


class Rectangle:

    def __init__(self, width: float = 0, height: float = 0):
        """
        >>> r = Rectangle(2, 3)
        >>> r.get_area()
        6.0
        >>> r.get_perimeter()
        10.0
        """
        self.set_dimensions(width, height)

    def set_dimensions(self, width: float, height: float):
        """
        >>> r = Rectangle(2, 3)
        >>> r.set_dimensions(5.0, 5.0)
        >>> r.get_area()
        25.0
        >>> r.get_perimeter()
        20.0
        >>> r.set_dimensions(-1, -1)
        Traceback (most recent call last):
        ...
        ValueError: Размер стороны прямоугольника не может быть отрицательной
        >>> r.set_dimensions(0, 0)
        >>> r.get_area()
        0.0
        >>> r.get_perimeter()
        0.0
        """
        if width < 0 or height < 0:
            raise ValueError("Размер стороны прямоугольника не может быть отрицательной")
        self._height = height
        self._width = width

    def get_area(self) -> float:
        """
        >>> r = Rectangle(5.0, 5.0)
        >>> r.get_area()
        25.0
        """""
        return float(self._width * self._height)

    def get_perimeter(self) -> float:
        """
        >>> r = Rectangle(5.0, 5.0)
        >>> r.get_perimeter()
        20.0
        """""
        return float(2 * (self._width + self._height))


if __name__ == "__main__":
    doctest.testmod()


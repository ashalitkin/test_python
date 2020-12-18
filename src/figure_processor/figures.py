

class Figure:

    def __str__(self):
        return "I am {0} with params: {1}".format(self.sayName(), self.tokens)

    def sayName(self):
        return self.__class__.__name__

    def _read(self):
        raise NotImplementedError

    def is_readable(self, str):
        raise NotImplementedError

    def read(self, str):
        if not self.is_readable(str):
            raise Exception("Can't read the string")
        self.tokens = str.split(" ")
        self._read()

    def _read_coord(self, str_coordinates):
        splitted_str = str_coordinates \
            .replace("(", "") \
            .replace(")", "") \
            .split(",")
        return [int(x) for x in splitted_str]
        return tuple(str_coordinates \
                     .replace("(", "") \
                     .replace(")", "") \
                     .split("."))

    def _multiply_coord(self, coord, multiplier):
        return tuple([c * multiplier for c in coord])


class Triangle(Figure):

    def square(self):
        a = ((self.point2[0] - self.point1[0]) ** 2 + (self.point2[1] - self.point1[1]) ** 2) ** 0.5
        b = ((self.point3[0] - self.point1[0]) ** 2 + (self.point3[1] - self.point1[1]) ** 2) ** 0.5
        c = ((self.point3[0] - self.point2[0]) ** 2 + (self.point3[1] - self.point2[1]) ** 2) ** 0.5
        p = (a + b + c) / 2.0
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s

    def is_readable(self, str):
        return str.startswith("T")

    def _read(self):
        if len(self.tokens) != 4:
            raise Exception("Some parameters are missing: {0}".format(self.tokens))

        self.point1 = self._read_coord(self.tokens[1])
        self.point2 = self._read_coord(self.tokens[2])
        self.point3 = self._read_coord(self.tokens[3])

    def multiple(self, multiplier):
        self.point1 = self._multiply_coord(self.point1, multiplier)
        self.point2 = self._multiply_coord(self.point2, multiplier)
        self.point3 = self._multiply_coord(self.point3, multiplier)


class Parallelagramm(Figure):

    def square(self):
        a = self.point2[0] - self.point1[0]
        h = self.point4[1] - self.point1[1]
        s = a * h
        return s

    def multiple(self, multiplier):
        self.point1 = self._multiply_coord(self.point1, multiplier)
        self.point2 = self._multiply_coord(self.point2, multiplier)
        self.point3 = self._multiply_coord(self.point3, multiplier)
        self.point4 = self._multiply_coord(self.point4, multiplier)

    def is_readable(self, str):
        return str.startswith("P")

    def _read(self):
        if len(self.tokens) != 5:
            raise Exception("Some parameters are missing: {0}".format(self.tokens))

        self.point1 = self._read_coord(self.tokens[1])
        self.point2 = self._read_coord(self.tokens[2])
        self.point3 = self._read_coord(self.tokens[3])
        self.point4 = self._read_coord(self.tokens[4])
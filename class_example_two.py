__author__ = "Bilal El Uneis"
__since__ = "September 2018"
__email__ = "bilaleluneis@gmail.com"


class Point2D:
    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.__x = x_coordinate
        self.__y = y_coordinate


class Point3D:
    def __init__(self, x_coordinate_3d: int, y_coordinate_3d: int, z_coordinate_3d: int):
        self.__point2D: Point2D = Point2D(x_coordinate_3d, y_coordinate_3d)
        self.__z: int = z_coordinate_3d


class Shape3D:
    def __init__(self, points: [Point3D]):
        self.__points_3d: [Point3D] = [Point3D] * 0
        for i in points:
            self.__points_3d.append(points[i])


class Triangle(Shape3D):

    def __init__(self, points_triangle: [Point3D]):
        super().__init__(points_triangle)


def main():
  counter: int = 0
  points: [Point3D] = [Point3D(0, 0, 0), Point3D(0, 0, 1)]
  line: Shape3D = Shape3D(points)
  triangle: Triangle = Triangle([Point3D(0, 0, 0), Point3D(0, 0, 1), Point3D(0, 1, 0)])


# start of running code
if __name__ == "__main__":
    main()

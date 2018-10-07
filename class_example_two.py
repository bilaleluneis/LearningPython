__author__ = "Bilal El Uneis"
__since__ = "September 2018"
__email__ = "bilaleluneis@gmail.com"


class Point2D:
    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.__x = x_coordinate
        self.__y = y_coordinate


class Point3D:
    def __init__(self, x_coordinate_3d: int, y_coordinate_3d: int, z_coordinate_3d: int):
        self.__point2D = Point2D(x_coordinate_3d, y_coordinate_3d)
        self.__z: int = z_coordinate_3d


class Shape3D:
    def __init__(self, points: [Point3D]):
        self.__points = points


class Sphere(Shape3D):

    __sphere_points = [Point3D]

    def __init__(self, center: Point3D, radius: int):
        super().__init__(Sphere.__sphere_points)
        self.__center_sphere = center
        self.__radius_sphere = radius


def main():
    Point3D(0, 0, 0)


# start of running code
if __name__ == "__main__":
    main()
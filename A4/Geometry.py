#  File: Geometry.py

#  Description: A program with classes involved in Solid Geometry and functions that find traits of classes.

#  Student Name: Srilakshmi Palanikumar

#  Student UT EID: sp49694

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: September 16, 2022

#  Date Last Modified: September 18, 2022

import math
import sys
import unittest

class Point(object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # string representation override
    def __str__(self):
        return "(" + (str(float(self.x))) + ", " + (str(float(self.y))) + ", " + (str(float(self.z))) + ")"

    # get the distance to another point
    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)

    # note floating point precision - finite bits for infinite numbers
    # cannot compare if the point is between two finite numbers.
    # workaround: take difference of two numbers. if absolute value of diff is less than a small number, they're equal
    def __eq__(self, other):
        # tol: arbitrarily small number, programmer's decision
        tol = 1.0e-6
        return ((abs(self.x - other.x)) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol)


class Sphere(object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.center = Point(x, y, z)
        self.radius = radius

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        radius = str(float(self.radius))
        return ("Center: " + str(self.center) + ", Radius: " + radius)

    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        return (4 * math.pi * (self.radius ** 2))

    # compute volume of a Sphere
    # returns a floating point number
    def volume(self):
        coeff = 4.0 / 3.0
        vol = coeff * math.pi * (self.radius ** 3)
        return vol

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point(self, p):
        return self.center.distance(p) < self.radius

    # determines if a point is outside a Sphere
    # p is a point object
    # returns a boolean
    def is_outside_point(self, p):
        return self.center.distance(p) > self.radius

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, other):
        dist_center = self.center.distance(other.center)
        return (dist_center + (other.radius)) < self.radius

    # determine if another Sphere is strictly outside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_outside_sphere(self, other):
        dist_center = self.center.distance(other.center)
        return (self.radius + (other.radius)) < dist_center

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        cube_vertices = Cube.to_points(a_cube)

        return (Sphere.is_inside_point(self, cube_vertices[0]) and Sphere.is_inside_point(self, cube_vertices[1]) and
                Sphere.is_inside_point(self, cube_vertices[2]) and Sphere.is_inside_point(self, cube_vertices[3]) and
                Sphere.is_inside_point(self, cube_vertices[4]) and Sphere.is_inside_point(self, cube_vertices[5]) and
                Sphere.is_inside_point(self, cube_vertices[6]) and Sphere.is_inside_point(self, cube_vertices[7]))

    # determine if a cube is strictly outside this sphere
    # a_cube is a cube object
    # returns a boolean
    def is_outside_cube(self, a_cube):
        cube_vertices = Cube.to_points(a_cube)

        return (Sphere.is_outside_point(self, cube_vertices[0]) and Sphere.is_outside_point(self, cube_vertices[1]) and
                Sphere.is_outside_point(self, cube_vertices[2]) and Sphere.is_outside_point(self, cube_vertices[3]) and
                Sphere.is_outside_point(self, cube_vertices[4]) and Sphere.is_outside_point(self, cube_vertices[5]) and
                Sphere.is_outside_point(self, cube_vertices[6]) and Sphere.is_outside_point(self, cube_vertices[7]))


      # determine if a Cylinder is strictly inside this Sphere
      # a_cyl is a Cylinder object
      # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        cyl_vertices = a_cyl.to_points()
        p0 = cyl_vertices[0]
        p1 = cyl_vertices[1]
        p2 = cyl_vertices[2]
        p3 = cyl_vertices[3]
        p4 = cyl_vertices[4]
        p5 = cyl_vertices[5]
        p6 = cyl_vertices[6]
        p7 = cyl_vertices[7]

        return ((self.is_inside_point(p0) and self.is_inside_point(p1) and self.is_inside_point(
            p2) and self.is_inside_point(p3) and self.is_inside_point(p4) and self.is_inside_point(
            p5) and self.is_inside_point(p6) and self.is_inside_point(p7)))

      # determine if another Sphere intersects this Sphere
      # other is a Sphere object
      # two spheres intersect if they are not strictly inside
      # or not strictly outside each other
      # returns a Boolean
    def does_intersect_sphere(self, other):
        sphere_inside = self.is_inside_sphere(other)
        sphere_outside = self.is_outside_sphere(other)

        return not(sphere_inside or sphere_outside)

      # determine if a Cube intersects this Sphere
      # the Cube and Sphere intersect if they are not
      # strictly inside or not strictly outside the other
      # a_cube is a Cube object
      # returns a Boolean
    def does_intersect_cube(self, a_cube):
        cube_inside = Sphere.is_inside_cube(self, a_cube)
        cube_outside = Sphere.is_outside_cube(self, a_cube)
        return (not cube_inside and not cube_outside)

      # return the largest Cube object that is circumscribed
      # by this Sphere
      # all eight corners of the Cube are on the Sphere
      # returns a Cube object
    def circumscribe_cube(self):
        cube_len = (self.radius * 2) / math.sqrt(3)
        circumscription = Cube(self.center.x, self.center.y, self.center.z, cube_len)
        return circumscription


class Cube(object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0, y=0, z=0, side=1):
        self.center = Point(x, y, z)
        self.side = side

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
        center = str(self.center)
        side = str(float(self.side))
        return ("Center: " + center + ", Side: " + side)

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):
        side_area = self.side ** 2
        area = side_area * 6
        return area

    # compute volume of a Cube
    # returns a floating point number
    def volume(self):
        return (self.side ** 3)

    # find all vertices of a cube object based on its center.
    # returns a list of tuples
    def vertices(self):
        radius = self.side / 2.0
        # q0 is the main point to reference
        q0 = (self.center.x + radius, self.center.y + radius, self.center.z + radius)

        # q0 and q1 show range of x coords
        q1 = (self.center.x - radius, self.center.y + radius, self.center.z + radius)

        # q0 and 2 show range of y coords
        q2 = (self.center.x + radius, self.center.y - radius, self.center.z + radius)

        # q0 and 3 show range of z coords
        q3 = (self.center.x + radius, self.center.y + radius, self.center.z - radius)

        # rest are for reference
        q4 = (self.center.x - radius, self.center.y - radius, self.center.z + radius)
        q5 = (self.center.x + radius, self.center.y - radius, self.center.z - radius)
        q6 = (self.center.x - radius, self.center.y + radius, self.center.z - radius)
        q7 = (self.center.x - radius, self.center.y - radius, self.center.z - radius)
        coords = [q0, q1, q2, q3, q4, q5, q6, q7]
        return coords

    # convert all vertices to point objects.
    # returns a list of point objects
    def to_points(self):
        cube_vertices = Cube.vertices(self)
        p0 = Point(cube_vertices[0][0], cube_vertices[0][1], cube_vertices[0][2])
        p1 = Point(cube_vertices[1][0], cube_vertices[1][1], cube_vertices[1][2])
        p2 = Point(cube_vertices[2][0], cube_vertices[2][1], cube_vertices[2][2])
        p3 = Point(cube_vertices[3][0], cube_vertices[3][1], cube_vertices[3][2])
        p4 = Point(cube_vertices[4][0], cube_vertices[4][1], cube_vertices[4][2])
        p5 = Point(cube_vertices[5][0], cube_vertices[5][1], cube_vertices[5][2])
        p6 = Point(cube_vertices[6][0], cube_vertices[6][1], cube_vertices[6][2])
        p7 = Point(cube_vertices[7][0], cube_vertices[7][1], cube_vertices[7][2])

        return [p0, p1, p2, p3, p4, p5, p6, p7]

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point(self, p):
        coords = Cube.vertices(self)
        return (coords[0][0] > p.x > coords[1][0]) and (coords[0][1] > p.y > coords[2][1]) and \
               (coords[0][2] > p.z > coords[3][2])

    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        envelop = Cube(a_sphere.center.x, a_sphere.center.y, a_sphere.center.z, (a_sphere.radius * 2))
        return self.is_inside_cube(envelop)

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube(self, other):
        main_coords = self.vertices()
        other_coords = other.vertices()

        check_x_upper = (main_coords[0][0] > other_coords[0][0] > main_coords[1][0])
        check_x_lower = (main_coords[0][0] > other_coords[1][0] > main_coords[1][0])
        check_y_upper = (main_coords[0][1] > other_coords[0][1] > main_coords[2][1])
        check_y_lower = (main_coords[0][1] > other_coords[2][1] > main_coords[2][1])
        check_z_upper = (main_coords[0][2] > other_coords[0][2] > main_coords[3][2])
        check_z_lower = (main_coords[0][2] > other_coords[3][2] > main_coords[3][2])

        return (check_x_upper and check_x_lower and check_y_upper and check_y_lower and check_z_upper and check_z_lower)

      # determine if a Cylinder is strictly inside this Cube
      # a_cyl is a Cylinder object
      # returns a Boolean
    def is_inside_cylinder(self, a_cyl):
        envelop = Cube(a_cyl.center.x, a_cyl.center.y, a_cyl.center.z, (a_cyl.radius * 2))
        return self.is_inside_cube(envelop)

      # determine if another Cube intersects this Cube
      # two Cube objects intersect if they are not strictly
      # inside and not strictly outside each other
      # other is a Cube object
      # returns a Boolean
    def does_intersect_cube(self, other):
        cube_vertices = other.to_points()
        p0 = cube_vertices[0]
        p1 = cube_vertices[1]
        p2 = cube_vertices[2]
        p3 = cube_vertices[3]
        p4 = cube_vertices[4]
        p5 = cube_vertices[5]
        p6 = cube_vertices[6]
        p7 = cube_vertices[7]

        return ((self.is_inside_point(p0) or self.is_inside_point(p1) or self.is_inside_point(
            p2) or self.is_inside_point(p3) or self.is_inside_point(p4) or self.is_inside_point(
            p5) or self.is_inside_point(p6) or self.is_inside_point(p7)))

      # determine the volume of intersection if this Cube
      # intersects with another Cube
      # other is a Cube object
      # returns a floating point number
    def intersection_volume (self, other):
        if self.does_intersect_cube(other):
            main_coords = self.vertices()
            other_coords = other.vertices()
            return 1
        else:
            return 0

      # return the largest Sphere object that is inscribed
      # by this Cube
      # Sphere object is inside the Cube and the faces of the
      # Cube are tangential planes of the Sphere
      # returns a Sphere object
    def inscribe_sphere(self):
        inscription = Sphere(self.center.x, self.center.y, self.center.z, (self.side / 2))
        return inscription


class Cylinder(object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.center = Point(x, y, z)
        self.radius = radius
        self.height = height

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        return "Center: " + str(self.center) + ", Radius: " + str(float(self.radius)) + ", Height: " + str(float(self.height))

    # compute surface area of Cylinder
    # returns a floating point number
    def area(self):
        lid_area = 2 * ((self.radius ** 2) * math.pi)
        rect_area = self.height * (2 * math.pi * self.radius)
        return lid_area + rect_area

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):
        vol = (self.radius ** 2) * math.pi * self.height
        return vol

    # create a list of "vertices" that cover the general shape of the cylinder
    # returns a list of Point objects
    def vertices(self):
        # q0 - q3 are upper circle points
        q0 = (self.center.x + self.radius, self.center.y, self.center.z + (self.height / 2))
        q1 = (self.center.x, self.center.y + self.radius, self.center.z + (self.height / 2))
        q2 = (self.center.x - self.radius, self.center.y, self.center.z + (self.height / 2))
        q3 = (self.center.x, self.center.y - self.radius, self.center.z + (self.height / 2))

        # rest are for lower circle
        q4 = (self.center.x + self.radius, self.center.y, self.center.z - (self.height / 2))
        q5 = (self.center.x, self.center.y + self.radius, self.center.z - (self.height / 2))
        q6 = (self.center.x - self.radius, self.center.y, self.center.z - (self.height / 2))
        q7 = (self.center.x, self.center.y - self.radius, self.center.z - (self.height / 2))

        coords = [q0, q1, q2, q3, q4, q5, q6, q7]
        return coords

    # convert all vertices to point objects.
    # returns a list of point objects
    def to_points(self):
        cyl_vertices = self.vertices()
        p0 = Point(cyl_vertices[0][0], cyl_vertices[0][1], cyl_vertices[0][2])
        p1 = Point(cyl_vertices[1][0], cyl_vertices[1][1], cyl_vertices[1][2])
        p2 = Point(cyl_vertices[2][0], cyl_vertices[2][1], cyl_vertices[2][2])
        p3 = Point(cyl_vertices[3][0], cyl_vertices[3][1], cyl_vertices[3][2])
        p4 = Point(cyl_vertices[4][0], cyl_vertices[4][1], cyl_vertices[4][2])
        p5 = Point(cyl_vertices[5][0], cyl_vertices[5][1], cyl_vertices[5][2])
        p6 = Point(cyl_vertices[6][0], cyl_vertices[6][1], cyl_vertices[6][2])
        p7 = Point(cyl_vertices[7][0], cyl_vertices[7][1], cyl_vertices[7][2])

        return [p0, p1, p2, p3, p4, p5, p6, p7]

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point(self, p):
        flat_diff = math.hypot(self.center.x - p.x, self.center.y - p.y)
        height_diff = math.sqrt(((self.center.z - p.z) ** 2))

        flat_int = flat_diff < self.radius
        height_int = height_diff < (self.height / 2)

        return flat_int and height_int

    # determine if a Point is strictly outside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_outside_point(self, p):
        flat_diff = math.hypot(self.center.x - p.x, self.center.y - p.y)
        height_diff = math.sqrt(((self.center.z - p.z) ** 2))

        flat_no_int = flat_diff > self.radius
        height_no_int = height_diff > (self.height / 2)

        return flat_no_int and height_no_int

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        # distance from center of cylinder to center of sphere in terms of x and y only
        flat_dist = math.hypot(self.center.x - a_sphere.center.x, self.center.y - a_sphere.center.y)
        flat_inside = (flat_dist + a_sphere.radius) < self.radius

        # check if inside in terms of z (height)
        height_dist = math.fabs(self.center.z - a_sphere.center.z)
        height_inside = (height_dist + a_sphere.radius) < (self.height / 2)

        return flat_inside and height_inside

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
      cube_vertices = Cube.to_points(a_cube)
      return (self.is_inside_point(cube_vertices[0]) and self.is_inside_point(cube_vertices[1])
              and self.is_inside_point(cube_vertices[2]) and self.is_inside_point(cube_vertices[3])
              and self.is_inside_point(cube_vertices[4]) and self.is_inside_point(cube_vertices[5])
              and self.is_inside_point(cube_vertices[6]) and self.is_inside_point(cube_vertices[7]))

    # determine if a cube is strictly outside of this Cylinder.
    # a_cube is a Cube object
    # returns a boolean
    def is_outside_cube(self, a_cube):
        cube_vertices = Cube.to_points(a_cube)
        return (self.is_outside_point(cube_vertices[0]) and self.is_outside_point(cube_vertices[1]) and
                self.is_outside_point(cube_vertices[2]) and self.is_outside_point(cube_vertices[3]) and
                self.is_outside_point(cube_vertices[4]) and self.is_outside_point(cube_vertices[5]) and
                self.is_outside_point(cube_vertices[6]) and self.is_outside_point(cube_vertices[7]))

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, other):
        flat_dist = math.hypot(self.center.x - other.center.x, self.center.y - other.center.y)
        flat_inside = (flat_dist + other.radius) < self.radius

        height_rad = other.height / 2
        height_dist = math.fabs(self.center.z - other.center.z)
        height_inside = (height_dist + height_rad) < (self.height / 2)

        return flat_inside and height_inside

    # determine if another Cylinder is strictly outside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_outside_cylinder(self, other):
        flat_dist = math.hypot(self.center.x - other.center.x, self.center.y - other.center.y)
        flat_outside = (flat_dist + other.radius) > self.radius

        height_rad = other.height / 2
        height_dist = math.fabs(self.center.z - other.center.z)
        height_outside = (height_dist + height_rad) > (self.height / 2)

        return flat_outside and height_outside

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder (self, other):
        is_inside = self.is_inside_cylinder(other)
        is_outside = self.is_outside_cylinder(other)

        return not(is_inside or is_outside)

def main():
    # set origin
    origin = Point(0, 0, 0)

    # read input line by line and assign tokens to the shapes' qualities they determine
    p_str = sys.stdin.readline().strip().split()
    p = Point(float(p_str[0]), float(p_str[1]), float(p_str[2]))
    q_str = sys.stdin.readline().strip().split()
    q = Point(float(q_str[0]), float(q_str[1]), float(q_str[2]))
    sa_str = sys.stdin.readline().strip().split()
    sphereA = Sphere(float(sa_str[0]), float(sa_str[1]), float(sa_str[2]), float(sa_str[3]))
    sb_str = sys.stdin.readline().strip().split()
    sphereB = Sphere(float(sb_str[0]), float(sb_str[1]), float(sb_str[2]), float(sb_str[3]))
    ca_str = sys.stdin.readline().strip().split()
    cubeA = Cube(float(ca_str[0]), float(ca_str[1]), float(ca_str[2]), float(ca_str[3]))
    cb_str = sys.stdin.readline().strip().split()
    cubeB = Cube(float(cb_str[0]), float(cb_str[1]), float(cb_str[2]), float(cb_str[3]))
    cya_str = sys.stdin.readline().strip().split()
    cylA = Cylinder(float(cya_str[0]), float(cya_str[1]), float(cya_str[2]), float(cya_str[3]), float(cya_str[4]))
    cyb_str = sys.stdin.readline().strip().split()
    cylB = Cylinder(float(cyb_str[0]), float(cyb_str[1]), float(cyb_str[2]), float(cyb_str[3]), float(cya_str[4]))

    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    pdist = p.distance(origin)
    qdist = q.distance(origin)
    if pdist > qdist:
        str = "is"
    else:
        str = "is not"
    print("Distance of Point p from the origin " + str + " greater than the distance of Point q from the origin")

    # print if Point p is inside sphereA
    p_in_sa = sphereA.is_inside_point(p)
    if p_in_sa:
        str = "is"
    else:
        str = "is not"
    print("Point p " + str + " inside sphereA")

    # print if sphereB is inside sphereA
    sb_in_sa = sphereA.is_inside_sphere(sphereB)
    if sb_in_sa:
        str = "is"
    else:
        str = "is not"
    print("sphereB " + str + " inside sphereA")

    # print if cubeA is inside sphereA
    ca_in_sa = sphereA.is_inside_cube(cubeA)
    if ca_in_sa:
        str = "is"
    else:
        str = "is not"
    print("cubeA " + str + " inside sphereA")

    # print if cylA is inside sphereA
    cya_in_sa = sphereA.is_inside_cyl(cylA)
    if cya_in_sa:
        str = "is"
    else:
        str = "is not"
    print("cylA " + str + " inside sphereA")

    # print if sphereA intersects with sphereB
    sa_int_sb = sphereA.does_intersect_sphere(sphereB)
    if sa_int_sb:
        str = "does"
    else:
        str = "does not"
    print("sphereA " + str + " intersect sphereB")

    # print if cubeB intersects with sphereB
    ca_int_sb = sphereB.does_intersect_cube(cubeB)
    if ca_int_sb:
        str = "does"
    else:
        str = "does not"
    print("cubeB " + str + " intersect sphereB")

    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA
    vol_cylA = cylA.volume()
    circ = sphereA.circumscribe_cube()
    vol_circ = circ.volume()
    if vol_circ > vol_cylA:
        str = "is"
    else:
        str = "is not"
    print("Volume of the largest Cube that is circumscribed by sphereA " + str + " greater than the volume of cylA")

    # print if Point p is inside cubeA
    p_in_ca = cubeA.is_inside_point(p)
    if p_in_ca:
        str = "is"
    else:
        str = "is not"
    print("Point p " + str + " inside cubeA")

    # print if sphereA is inside cubeA
    sa_in_ca = cubeA.is_inside_sphere(sphereA)
    if sa_in_ca:
        str = "is"
    else:
        str = "is not"
    print("sphereA " + str + " inside cubeA")

    # print if cubeB is inside cubeA
    cb_in_ca = cubeA.is_inside_cube(cubeB)
    if cb_in_ca:
        str = "is"
    else:
        str = "is not"
    print("cubeB " + str + " inside cubeA")

    # print if cylA is inside cubeA
    cya_in_ca = cubeA.is_inside_cylinder(cylA)
    if cya_in_ca:
        str = "is"
    else:
        str = "is not"
    print("cylA " + str + " inside cubeA")

    # print if cubeA intersects with cubeB
    ca_int_cb = cubeA.does_intersect_cube(cubeB)
    if ca_int_cb:
        str = "does"
    else:
        str = "does not"
    print("cubeA " + str + " intersect cubeB")

    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    ca_vol_cb = cubeA.intersection_volume(cubeB)
    sa_vol = sphereA.volume()
    if ca_vol_cb > sa_vol:
        str = "is"
    else:
        str = "is not"
    print("Intersection volume of cubeA and cubeB " + str + " greater than the volume of sphereA")

    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    inscribed = cubeA.inscribe_sphere()
    inscribed_area = inscribed.area()
    cyl_area = cylA.area()
    if inscribed_area > cyl_area:
        str = "is"
    else:
        str = "is not"
    print("Surface area of the largest Sphere object inscribed by cubeA " + str +
          " greater than the surface area of cylA")

    # print if Point p is inside cylA
    p_in_cya = cylA.is_inside_point(p)
    if p_in_cya:
        str = "is"
    else:
        str = "is not"
    print("Point p " + str + " inside cylA")

    # print if sphereA is inside cylA
    sa_in_cya = cylA.is_inside_sphere(sphereA)
    if sa_in_cya:
        str = "is"
    else:
        str = "is not"
    print("sphereA " + str + " inside cylA")

    # print if cubeA is inside cylA
    ca_in_cya = cylA.is_inside_cube(cubeA)
    if ca_in_cya:
        str = "is"
    else:
        str = "is not"
    print("cubeA " + str + " inside cylA")

    # print if cylB is inside cylA
    cyb_in_cya = cylA.is_inside_cylinder(cylB)
    if cyb_in_cya:
        str = "is"
    else:
        str = "is not"
    print("cylB " + str + " inside cylA")

    # print if cylB intersects with cylA
    cya_int_cyb = cylA.does_intersect_cylinder(cylB)
    if cya_int_cyb:
        str = "does"
    else:
        str = "does not"
    print("cylB " + str + " intersect cylA")

if __name__ == "__main__":
  main()
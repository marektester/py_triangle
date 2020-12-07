def check_triangle(x, y, z):
    if not check_value(x) or not check_value(y) or not check_value(z) or (x + y <= z) or (x + z <= y) or (y + z <= x):
        return "Error! Invalid data. Not a triangle."
    elif x == y == z:
        return "Equilateral Triangle"
    elif x == y or y == z or z == x:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"


def check_value(val):
    return isinstance(val, int) and val > 0


if __name__ == '__main__':
    print("Input lengths of the triangle sides (int):")
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        z = int(input("z: "))
    except:
        print("Invalid data, please enter integer values!")
    else:
        print(check_triangle(x, y, z) + " (%d, %d, %d)" % (x, y, z))


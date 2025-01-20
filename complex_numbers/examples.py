from complex import Complex

def demonstration():
    z = Complex(1, -2)
    y = Complex(-3, 4)

    print(f'z = {z}') # -->  1 + 2i


    print(f'z.re() = {z.re()}') # -->  1
    print(f'z.im() = {z.im()}') # -->  2

    print(f'Complex() gives: {Complex()}') # --> 0 + 0i
    print(f'Complex(5) gives: {Complex(5)}') # --> 5 + 0i
    print(f'Complex(0, 4) gives: {Complex(0, 4)}')


    print(f'z + y = {z + y}')
    print(f'z - y = {z - y}')

    print(f'z + 3 = {z + 3}')
    print(f'3 + z = {3 + z}')
    print(f'z * 3 = {z * 3}')
    print(f'3 * z = {3 * z}')
    print(f'z / 3 = {z / 3}')
    print(f'3 / z = {3 / z}')
    print(f'z * y = {z * y}')

    print(f'z == y gives: {z == y}')
    print(f'z != y gives: {z != y}')

    print(f'z.conjugate() gives: {z.conjugate()}')
    print(f'y.conjugate() gives: {y.conjugate()}')

demonstration()


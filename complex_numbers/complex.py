
class Complex:

    def __init__(self, re=None, im=None):

        if isinstance(re, (int, float)):
            self._re = re
        elif isinstance(re, str):
            raise ValueError("Input 're' must be of type 'int' or 'float'")
        else:
            self._re = 0

        if isinstance(im, (int, float)):
            self._im = im
        elif isinstance(im, str):
            raise ValueError("Input 'im' must be of type 'int' or 'float'")
        else:
            self._im = 0

    # Bestemmer at self._re og self._im skal være av typen int hvis mulig
    @property
    def real(self):
        try:
            self._re = int(self._re)
        except ValueError or TypeError:
            pass

    @property
    def imaginary(self):
        try:
            self._re = int(self._re)
        except ValueError or TypeError:
            pass

    # Definerer spesifikk representasjon (tallform) ut ifra hvilke kombinasjoner av self._re
    # og self._im som kan forekomme
    def __str__(self):

        # In the __str__-representation we have chosen to represent a Complex([number]) as just
        # the real number, and Complex(0, [number]) as [number]*i. This is according to the definition
        # of complex numbers, and will optimize their readability.
        if self._im == 1:
            return f'{self._re} + i'
        elif self._im == -1:
            return f'{self._re} - i'
        elif self._re == 0 and self._im != 0:
            return f'{self._im}i'
        elif self._im > 0:
            return f'{self._re} + {self._im}i'
        elif self._im == 0:
            return str(self._re)
        else:
            return f'{self._re} - {abs(self._im)}i'

    # Prosedyrer for å returnere reell og imaginær del fra ethvert komplekst tall
    def re(self):
        return self._re

    def im(self):
        return self._im

    # I hver regneoperasjonsfunksjon tar jeg høyde for at det kan regnes med enten komplekse eller
    # reelle tall
    def __add__(self, other):

        assert isinstance(other, (Complex, int, float)), 'All operands must have numerical values'

        if isinstance(other, (int, float)):
            other = Complex(other)

        return Complex(self._re + other.re(), self._im + other.im())

    def __radd__(self, other):

        assert isinstance(other, (Complex, int, float)), 'All operands must have numerical values'

        if isinstance(other, (int, float)):
            other = Complex(other)

        return Complex(self._re + other.re(), self._im + other.im())

    def __sub__(self, other):

        assert isinstance(other, (Complex, int, float)), 'All operands must have numerical values'
        if isinstance(other, (int, float)):
            other = Complex(other)

        return Complex(self._re - other.re(), self._im - other.im())

    def __rsub__(self, other):

        assert isinstance(other, (Complex, int, float)), 'All operands must have numerical values'

        if isinstance(other, (int, float)):
            other = Complex(other)

        return Complex(self._re - other.re(), self._im - other.im())

    def __mul__(self, other):

        assert isinstance(other, (Complex, int, float)), 'All operands must have numerical values'

        if isinstance(other, (int, float)):
            other = Complex(other)
        return Complex(
            self._re * other.re() - self._im * other.im(),
            self._re * other.im() + self._im * other.re()
        )

    def __rmul__(self, other):

        assert isinstance(other, (Complex, int, float)), 'All operands must have numerical values'

        if isinstance(other, (int, float)):
            other = Complex(other)
        return Complex(
            self._re * other.re() - self._im * other.im(),
            self._re * other.im() + self._im * other.re()
        )

    def __truediv__(self, other):

        assert isinstance(other, (Complex, int, float)), 'All operands must have numerical values'

        if isinstance(other, (int, float)):
            other = Complex(other)
        return Complex(
            (self._re * other.re() + self._im * other.im()) / (other.re() ** 2 + other.im() ** 2),
            (self._im * other.re() - self._re * other.im()) / (other.re() ** 2 + other.im() ** 2)
        )



    def __rtruediv__(self, other):

        assert isinstance(other, (Complex, int, float)), 'All operands must have numerical values'

        if isinstance(other, (int, float)):
            other = Complex(other)
            return Complex(
                (self._re * other.re() + self._im * other.im()) / (self._re ** 2 + self._im ** 2),
                (self._re * other.im() - self._im * other.re()) / (self._re ** 2 + self._im ** 2)
            )


    def __eq__(self, other):

        assert isinstance(other, (Complex, float, int)), 'All operands must have numerical values'

        if isinstance(other, Complex):
            return self._re == other.re() and self._im == other.im()
        else:
            if self._im == 0:
                return other == self._re
            else:
                return False


    def __ne__(self, other):
        if isinstance(other, Complex):
            return self._re != other.re() or self._im != other.im()

    def conjugate(self):
        return Complex(-self._re, -self._im)


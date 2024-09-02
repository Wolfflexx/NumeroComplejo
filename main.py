class ComplexNumber:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __str__(self) -> str:
        """Representación en cadena del número complejo."""
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {-self.imaginary}i"

    def add(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """Suma de dos números complejos."""
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def subtract(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """Resta de dos números complejos."""
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def multiply(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """Multiplicación de dos números complejos."""
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def divide(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """División de dos números complejos."""
        denominator = other.real ** 2 + other.imaginary ** 2
        if denominator == 0:
            raise ValueError("No se puede dividir por un número complejo con parte real e imaginaria ambas iguales a 0.")
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real_part, imaginary_part)

# Ejemplo de uso
num1 = ComplexNumber(3, 2)
num2 = ComplexNumber(1, 7)

print("Número complejo 1:", num1)
print("Número complejo 2:", num2)

print("Suma:", num1.add(num2))
print("Resta:", num1.subtract(num2))
print("Multiplicación:", num1.multiply(num2))
print("División:", num1.divide(num2))

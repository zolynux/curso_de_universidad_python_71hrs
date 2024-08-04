class ConvertirTemperatura:
    # * Convertir de temperatura en Python

    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def c_f(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f"Temperatura C demasiado alta: {celsius}")
        return celsius * 9 / 5 + 32

    @classmethod
    def f_c(cls, fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f"Temperatura F demasiado alta: {fahrenheit}")
        return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    resultado = ConvertirTemperatura.c_f(15)
    print(f"15 C a F: {resultado:.2f}")
    resultado = ConvertirTemperatura.f_c(10)
    print(f"10 F a C: {resultado:.2f}")

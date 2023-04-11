from utils import welcome_message

unidades = [
    "cero",
    "uno",
    "dos",
    "tres",
    "cuatro",
    "cinco",
    "seis",
    "siete",
    "ocho",
    "nueve",
]
decenas = [
    "diez",
    "once",
    "doce",
    "trece",
    "catorce",
    "quince",
    "dieciséis",
    "diecisiete",
    "dieciocho",
    "diecinueve",
]
decenas2 = [
    "veinte",
    "treinta",
    "cuarenta",
    "cincuenta",
    "sesenta",
    "setenta",
    "ochenta",
    "noventa",
]
centenas = [
    "cien",
    "doscientos",
    "trescientos",
    "cuatrocientos",
    "quinientos",
    "seiscientos",
    "setecientos",
    "ochocientos",
    "novecientos",
]
unidades_millar = ["mil", "un millón"]


def app(numero):
    if numero < 0 or numero > 1000000:
        return "El número está fuera del rango permitido."
    else:
        if numero == 0:
            return "cero"

        # Números del 1 al 9
        if numero <= 9:
            return unidades[numero]

        # Números del 10 al 19
        if numero <= 19:
            return decenas[numero - 10]

        # Números del 20 al 99
        if numero <= 99:
            if numero % 10 == 0:
                return decenas2[int(numero / 10) - 2]
            else:
                return decenas2[int(numero / 10) - 2] + " y " + unidades[numero % 10]

        # Números del 100 al 999
        if numero <= 999:
            if numero == 100:
                return centenas[0]
            elif numero % 100 == 0:
                return centenas[int(numero / 100) - 1]
            else:
                return centenas[int(numero / 100) - 1] + " " + app(numero % 100)

        # Números del 1000 al 999999
        if numero <= 999999:
            if numero == 1000:
                return unidades_millar[0]
            elif numero % 1000 == 0:
                return app(int(numero / 1000)) + " " + unidades_millar[0]
            elif numero < 2000:
                return "mil " + app(numero % 1000)
            else:
                return (
                    app(int(numero / 1000))
                    + " "
                    + unidades_millar[0]
                    + " "
                    + app(numero % 1000)
                )

        # Número 1000000
        if numero == 1000000:
            return unidades_millar[1]


if __name__ == "__main__":
    print(welcome_message())
    numero = int(input("Ingrese el número que desea convertir: "))
    print(app(numero))

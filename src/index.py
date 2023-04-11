from app import app
from utils.welcome_message import welcome_message


if __name__ == "__main__":
    print(welcome_message())
    numero = int(input("Ingrese el número que desea convertir: "))
    print(app(numero))

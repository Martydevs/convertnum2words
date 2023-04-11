from colorama import init, Fore, Style
import pyfiglet

init(autoreset=True)


def welcome_message():
    text = pyfiglet.figlet_format("Number2Word", font="big")
    result = Fore.RED + Style.BRIGHT + text + Style.RESET_ALL
    return f"{result} \n  Una Aplicacion simple hecha en Python que convierte un numero a palabras. \n  Hecho por: André Martí, Gerardo Arredondo y Said Velazquez \n  Version: 1.0.0 \n  Repositorio: https://github.com/Martydevs/convertnum2words.git \n"

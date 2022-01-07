"""El modulo mypy se complementa con el modulo typing ya que permitirá mostrar los errores de 
tipado débil en Python.
Para revisar si algún archivo contiene errores de tipado ejecutamos en la línea de comandos 
lo siguiente: 
mypy archivo.py --check-untyped-defs"""


def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string==string[::-1]    


def primo(int:int) -> bool:
    return int%2!=0

def run():
    print(is_palindrome("ana"))
    print(primo(7))


if __name__ == "__main__":
    run()
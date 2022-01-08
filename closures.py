def make_repeater_of(n):
    def repeater(string):
        assert type(string) != string, "Solo se puede utilizar cadenas"
        return string * n
    return repeater

def make_division_by(n):
    def repeater(num):
        assert num == 0 or n == 0, "No se puede dividir entre cero"
        return num / n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("hola"))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))


if __name__ == "__main__":
    run()    
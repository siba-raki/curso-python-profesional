from datetime import datetime
import pandas as pd
from pandas.io.formats.format import Datetime64TZFormatter #no tengo pandas instalado en este venv)

def excecution_time(func):  
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Pasaron {time_elapsed.total_seconds()} segundos")
    return wrapper

@excecution_time
def random_func():
    for _ in range(1, 1000000):
        pass


def suma(a: int, b: int) -> int:
    return a + b


def description(func):
    def wrapper():
        func()
        print(f'El tamano del data set es: {func().shape}')
        print(f'Los tipos de datos del dataset son:\n{func().dtypes}')
    return wrapper


@description
def read_csv(dir):
    df = pd.read_csv(dir)
    return df


suma(5, 5)
# random_func()


class Persona:

    def __init__(self, nombre: str = "Martino", apellido: str = "Vespa", dni: str = "45141174"):

        __atributo1__=0

        self.__nombre__ = nombre

        self.__apellido__ = apellido

        self.__dni__ = dni

    def mostrar_datos(self):

        print(f'Los datos mios son nombre = {self.__nombre__} apellido = {self.__apellido__} documento = {self.__dni__}')
        
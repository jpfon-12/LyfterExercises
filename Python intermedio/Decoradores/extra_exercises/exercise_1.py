# Cree una función que imprima “Hola, [nombre]” dos veces:
# Cree un decorador @repeat_twice que haga que la función decorada se ejecute dos veces seguidas, con los mismos argumentos

class User:

    def repeat_twice(func):
        def wrapper(name):
            for _ in range(2):
                func(name)
        return wrapper

    @repeat_twice
    def printing_hello(name):
        print(f"Hello {name}")


user1 = User
user1.printing_hello("Juan")
# Cree una clase de User que:
# Tenga un atributo de date_of_birth.
# Tenga un property de age.
# Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.

from datetime import date

class User:

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        age = date.today().year - self.date_of_birth.year
        if(date.today().month, date.today().day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


def verify_adult(func):
    def wrapper(user):
        if user.age < 18:
            raise ValueError(
                    "Error. User is under 18 years old"
                    )
        func(user)
    return wrapper


@verify_adult
def get_user(user):
    print(f"User: {user.name}")
    print(f"Age: {user.age}")


user1 = User("Juan", date(2000,12,21))
get_user(user1)
# print(user1.age)
# print(user1.__dict__)

# Cree un decorador @requires_login que:
# Verifique si la variable global user_logged_in es True
# Si no lo es, debe lanzar una excepción "Usuario no autenticado"
# Si lo es, la función decorada se ejecuta normalmente

user_logged_in = False

class UserLogin:
    def __init__(self):
        global user_logged_in
        user_logged_in = True


    def requires_login(func):
        def wrapper(*args):
            if user_logged_in == False:
                raise ValueError(
                    "User not authenticated"
                )
            return func(*args)
        return wrapper
    

    @requires_login
    def view_profile(self):
        print("Showing user's profile")


login = UserLogin()
login.view_profile()



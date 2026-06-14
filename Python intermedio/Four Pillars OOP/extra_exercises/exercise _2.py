# Cree una clase abstracta User con los siguientes métodos abstractos:
# get_role()
# has_permission(permission)
# Luego cree dos clases que hereden de ella:
# AdminUser
# RegularUser
# Cada una debe implementar los métodos
# Por ejemplo:
# AdminUser siempre tiene permisos
# RegularUser solo tiene permisos limitados ("read", por ejemplo)

from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):
    def get_role(self):
        return (f"{self.name}: Admin user")
    
    def has_permission(self, permission):
        permission_right = False
        if permission.lower() == "delete" or permission.lower() == "read" or permission.lower() == "execute" or permission.lower() == "write":
            permission_right = True
        return permission_right



class RegularUser(User):
    def get_role(self):
        return (f"{self.name}: Regular user")
    
    def has_permission(self, permission):
        permission_right = False
        if permission.lower() == "read":
            permission_right = True
        elif permission.lower() == "delete" or permission.lower() == "execute" or permission.lower() == "write":
            permission_right = False
        return permission_right


user1 = AdminUser("Carlos")
print(user1.get_role())
print(user1.has_permission("execute"))

user2 = RegularUser("Ana")
print(user2.get_role())
print(user2.has_permission("execute"))

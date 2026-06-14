# Cree una clase Employee con los siguientes requisitos:
# Atributos privados: _name, _salary
# Use @property y @<atributo>.setter para:
# Mostrar el nombre y el salario
# Validar que el salario nunca sea negativo
# Cree un método promote que aumente el salario un porcentaje definido

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary

    @property
    def name(self):
        return self._name
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = salary


    def promote(self, percentage):
        self.promoted_salary = self._salary * percentage
        self._salary = self._salary + self.promoted_salary 


try:
    employee = Employee("Ana", -1000)
    employee.promote(0.1)

    print(f"Employee: {employee.name}")
    print(f"Salary after promotion: {employee.salary}")

except ValueError as ex:
    print(f"Error: {ex}")



class grandpa:

    def __init__(self, car, pension):
        self.car = car
        self.pension = pension

    def _get_granpa_car_details(self):
        return f"You can drive my car - Grandpa"
    
    def __get_grandpa_pension_details(self):
        return f"You can't access my pension - Grandpa"
    
class papa(grandpa):

    def __init__(self, car, salary):
        self.salary = salary
        grandpa.__init__(self, car, self.salary * 0.5)

    def _get_papa_car(self):
        return self._get_granpa_car_details()
    
    def _get_papa_pension_details(self):
        return self.__get_grandpa_pension_details()
    
class son(papa):

    def __init__(self, car, papa_salary):
        papa.__init__(self, car, papa_salary)

    def get_grandpa_car(self):
        return self._get_papa_car()
    
    def get_grandpa_pension(self):
        return self._get_papa_pension_details()
    
# grandpaIns = grandpa('Swift', 50000)
# print(grandpaIns._get_granpa_car_details())
# print(grandpaIns.__get_grandpa_pension_details())

# papaIns = papa('Swift', 100000)
# print(papaIns._get_papa_car())
# print(papaIns._get_papa_pension_details())

sonIns = son("Swift", 100000)
print(sonIns.get_grandpa_car())
print(sonIns.get_grandpa_pension())
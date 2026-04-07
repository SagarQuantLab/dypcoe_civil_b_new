class Car:

    def __init__(self, car_name, model_year):
        self._name = car_name
        self.__year = model_year

    def _get_my_car_details(self):
        return f"Car name {self._name} and year of manufacture {self.__year}"
    
    def __get_registeration_details(self):
        return "No registeration details found"

carIns = Car('Swift', 2026)
print(carIns._get_my_car_details())
# print(carIns.__year)
# print(carIns.__get_registeration_details())
# solution-1
# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand 
#         self.model = model

# my_car = Car("lemborghini","huracan")
# print(my_car.brand)
# print(my_car.model)



# solution-2
# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand 
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"

# my_car = Car("ferrari","488 pista")
# print(my_car.full_name())



# solution-3
# class Car:
#      def __init__(self,brand,model):
#          self.brand = brand 
#          self.model = model

#      def full_name(self):
#          return f"{self.brand} {self.model}"
     
# class ElectricCar(Car):
#     def __init__(self,brand ,model, battry_size):
#         self.battry_size=battry_size
#         super().__init__(brand,model)

# my_tesla = ElectricCar("tesla","s plaid","180kwh")
# print(my_tesla.battry_size)
# print(my_tesla.model)
# print(my_tesla.full_name())




# solution-4
# class Car:
#      def __init__(self,brand,model):
#          self.__brand = brand 
#          self.model = model

#      def full_name(self):
#          return f"{self.__brand} {self.model}"
     
#      def get_brand(self):
#          return self.__brand
     
# class ElectricCar(Car):
#     def __init__(self,__brand ,model, battry_size):
#         self.battry_size=battry_size
#         super().__init__(__brand,model)

# my_tesla = ElectricCar("tesla","s plaid","180kwh")
# print(my_tesla.battry_size)
# print(my_tesla.get_brand())




# solution-5
# class Car:
#      def __init__(self,brand,model):
#          self.__brand = brand 
#          self.model = model

#      def full_name(self):
#          return f"{self.__brand} {self.model}"
     
#      def get_brand(self):
#          return self.__brand
     
#      def fuel_type(self):
#          return "petrol or diesel"
     
# class ElectricCar(Car):
#     def __init__(self,__brand ,model, battry_size):
#         self.battry_size=battry_size
#         super().__init__(__brand,model)

#     def fuel_type(self):
#          return "Electric charge"

# my_tesla = ElectricCar("tesla","s plaid","180kwh")
# print(my_tesla.fuel_type())

# my_car = Car("Lemborghini","Huracan")
# print(my_car.fuel_type())




# solution-6
# class Car:
#      total_car = 0

#      def __init__(self,brand,model):
#          self.__brand = brand 
#          self.__model = model
#          Car.total_car += 1

#      def full_name(self):
#          return f"{self.__brand} {self.__model}"
     
#      def get_brand(self):
#          return self.__brand
     
#      def fuel_type(self):
#          return "petrol or diesel"
     
# class ElectricCar(Car):
#     def __init__(self,__brand ,__model, battry_size):
#         self.battry_size=battry_size
#         super().__init__(__brand,__model)

#     def fuel_type(self):
#          return "Electric charge"
    
#     @staticmethod
#     def generel_description():
#          return "cars are means of transport"
    
#     @property
#     def model(self):
#         return self.__model

# my_tesla = ElectricCar("tesla","s plaid","180kwh")
# print(my_tesla.fuel_type())

# my_car = Car("Lemborghini","Huracan")
# my_car = Car("Lemborghini","urus")
# print(my_car.fuel_type())

# print(Car.total_car)








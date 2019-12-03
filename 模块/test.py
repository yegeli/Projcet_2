class Car():
    """模拟汽车"""
    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 10
    def get_descriptive_cars(self):
        name = str(self.year) + ' ' + self.make + ' ' + self.model
        return name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles.")
    def updata_odometer(self , mileage):
        self.odometer_reading += mileage
class Battery():
    def __init__(self , battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
class ElectricCar(Car):
    def __init__(self, make , model , year):
        super().__init__(make, model , year)
        self.battery = Battery()

my_Tesla = ElectricCar('Tesla' , 'model_s' , '2016')
print(my_Tesla.get_descriptive_cars())
my_Tesla = Battery(80)
# print(my_Tesla.battery_size)
my_Tesla.battery.describe_battery()
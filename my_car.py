from car import Car
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descripted_name())
my_new_car.odometer_reading = 50
my_new_car.read_odometer()
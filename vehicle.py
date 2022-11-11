class Vehicle:
    def __init__(self, name, max_speed, km_per_liter):
        self.name = name
        self.max_speed = max_speed
        self.km_per_liter = km_per_liter

    def num_seats(self, capacity):
        print(f'The maximum seating capacity of the {self.name} vehicle is {capacity}')

    def toPrint(self):
        print(f'Name of the vehicle: {self.name}')
        print(f'Maximum speed: {self.max_speed} km/h')
        print(f'Kilometers traveled per liter: {self.km_per_liter}')


car = Vehicle('Lamborghini', 350, 10)
car.toPrint()


class Bus(Vehicle):
    def num_seats(self, capacity=70):
        return super().num_seats(capacity=70)


school_bus = Bus('Scania', 120, 8)
school_bus.toPrint()
school_bus.num_seats()

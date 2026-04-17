
class Vehicle():
    def drive(self):
        print('Run')
class Sedan(Vehicle):
    def drive(self):
        print('Run Sedan')
class Truck(Vehicle):
    def drive(self):
        print('Run Truck')
class Boat():
    def drive(self):
        print('Fly')


def drive(vehicle):
    if isinstance(vehicle, Vehicle):
        vehicle.drive()

sedan = Sedan()
drive(sedan)    # drive(sedan)

truck = Truck()
drive(truck)    # Run Truck

boat = Boat()
drive(boat)     # 아무것도 안나옴: Vehicle을 상속받지 않았기 때문
